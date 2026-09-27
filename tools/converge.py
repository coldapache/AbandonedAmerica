#!/usr/bin/env python
"""
Converge every branch's verified work into origin/main.

The repo accumulated ~460 unmerged branches, all editing the same CSV. Many
forked from OLD versions of main, so a plain `git merge` would revert thousands
of rows. This does a per-row 3-way merge instead:

    base   = CSV at the branch's merge-base with origin/main
    main   = CSV at origin/main
    theirs = CSV at the branch tip

For each address key:
    t == b            -> branch did not touch the row      -> main stands
    o == b, t is None -> branch deleted it, main did not   -> deletion wins
    o == b, t is not None and b is None  -> branch added it   -> added
    o == b, t != b                       -> branch edited it  -> edit wins
    otherwise         -> both sides changed it: deletion still wins (a branch
                         that genuinely removed the row is expressing an audit
                         finding), otherwise main's version stands

Deletions are only applied when the branch actually deleted the row relative to
its own base (this is what makes it a genuine intent rather than a stale fork).
`git log -S` cannot be used for this: `--all` walks other branches' history, so
it reports a row as removed by every later commit on the repo. Always diff a
branch against its own merge-base.

Usage:
    python temp/converge.py            # report only
    python temp/converge.py --write    # write the merged CSV

New rows from a "burned" producer class are dropped by default (--keep-burned to
include them). The audit campaign burned whole producer classes for producing
false positives at sustained high rates (e.g. Buffalo VBR 100%, rust-belt-oh
86%, paterson-vbr 50%), and the branches that re-add rows from those same
classes re-import exactly the unverified pattern that was purged. CLAUDE.md
requires visual confirmation before adding, so those do not count as verified.
"""
import argparse
import collections
import csv
import io
import json
import os
import re
import subprocess
import sys

CSV = "Abandoned America - Abandoned or Unused Properties.csv"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(*args, stdin=None):
    r = subprocess.run(["git"] + list(args), cwd=REPO, capture_output=True, input=stdin)
    if r.returncode != 0:
        raise RuntimeError("git %s -> %s" % (" ".join(args), r.stderr.decode("utf-8", "replace")))
    return r.stdout


def akey(s):
    """Identity of a property: normalized address."""
    return re.sub(r"[.,]", "", re.sub(r"\s+", " ", s.upper()).strip())


def parse(text):
    """Parse CSV text -> (fieldnames, {akey: rowdict}), preserving row order."""
    if isinstance(text, bytes):
        text = text.decode("utf-8", "replace")
    text = text.lstrip("\ufeff")
    rd = csv.DictReader(io.StringIO(text, newline=""))
    rows = collections.OrderedDict()
    for row in rd:
        if not row.get("address"):
            continue
        rows[akey(row["address"])] = {k: (v or "").strip() for k, v in row.items()}
    return rd.fieldnames, rows


def read_blobs(specs):
    """specs: ['rev:path', ...] -> {rev: csv_text}. Batched to dodge argv limits."""
    out = {}
    B = 200
    for i in range(0, len(specs), B):
        chunk = specs[i:i + B]
        stdin = ("\n".join(chunk) + "\n").encode()
        data = git("cat-file", "--batch", stdin=stdin)
        pos = 0
        for spec in chunk:
            nl = data.index(b"\n", pos)
            parts = data[pos:nl].decode().split()
            pos = nl + 1
            if len(parts) < 3:
                out[spec] = None
                continue
            size = int(parts[2])
            out[spec] = data[pos:pos + size].decode("utf-8", "replace")
            pos += size + 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="write the merged CSV")
    ap.add_argument("--keep-burned", action="store_true",
                    help="also import new rows from producer classes that were burned")
    ap.add_argument("--out", default=CSV)
    ap.add_argument("--report", default=os.path.join("temp", "converge-report.json"))
    args = ap.parse_args()

    main_sha = git("rev-parse", "origin/main").decode().strip()

    # Every local branch that is ahead of origin/main.
    branches = git("for-each-ref", "refs/heads", "--format=%(refname:short)").decode().split()
    ahead = [b for b in branches if git("rev-list", "--count", "origin/main..%s" % b).decode().strip() != "0"]
    print("branches ahead of origin/main: %d" % len(ahead))

    # Resolve merge-base + CSV blob for each branch
    bases = {}
    for b in ahead:
        bases[b] = git("merge-base", "origin/main", b).decode().strip()

    specs, seen = [], set()
    for b in ahead:
        for rev in (b, bases[b]):
            if rev not in seen:
                seen.add(rev)
                specs.append("%s:%s" % (rev, CSV))
    specs.insert(0, "%s:%s" % (main_sha, CSV))
    texts = read_blobs(specs)

    _, main_rows = parse(texts["%s:%s" % (main_sha, CSV)])
    print("origin/main rows: %d" % len(main_rows))

    added = {}                                                   # akey -> (rowdict, {branches})
    deleted = collections.defaultdict(list)                      # akey -> [branches]
    edited = collections.defaultdict(list)                       # akey -> [(branch, rowdict)]
    conflicted = collections.defaultdict(list)                   # akey -> [branches] both sides moved
    conflicts = collections.defaultdict(list)                    # akey -> [branches] conflicts that stayed on main

    for b in ahead:
        _, base = parse(texts["%s:%s" % (bases[b], CSV)])
        _, theirs = parse(texts["%s:%s" % (b, CSV)])
        for k in set(base) | set(main_rows) | set(theirs):
            bv, ov, tv = base.get(k), main_rows.get(k), theirs.get(k)
            if tv == bv:
                continue                       # branch never touched this row
            if ov == bv:                       # main never touched it -> branch intent wins
                if tv is None:
                    deleted[k].append(b)
                elif bv is None:
                    added.setdefault(k, (tv, []))[1].append(b)
                else:
                    edited[k].append((b, tv))
            else:
                conflicted[k].append(b)
                if tv is not None:             # row survives -> main's version stands
                    conflicts[k].append(b)

    fields = list(parse(texts["%s:%s" % (main_sha, CSV)])[0])

    # Producer classes burned by the audit campaign. New rows whose source (or
    # branch) matches one of these are the same unverified pattern that was
    # purged, so they are dropped unless --keep-burned.
    BURNED_SIGNATURES = (
        ("clarksville", ("mcgtn", "montgomery county parcels")),
        ("covington", ("linkgis", "link-gis")),
        ("lexington", ("lfucg", "vpr-certified", "lexingtonky.gov")),
        ("nashville", ("property standards violations", "data.nashville.gov")),
        ("owensboro", ("ompc", "gis.owensboro.org")),
    )

    def burned(row, branch):
        hay = ((row.get("source") or "") + " " + (row.get("notes") or "")).lower()
        return any(k in branch or any(s in hay for s in sig)
                   for k, sig in BURNED_SIGNATURES)

    # Apply: keep main's order, drop deleted, override edited, append new (stable sort by state/city).
    result = collections.OrderedDict()
    applied_del = applied_edit = 0
    for k, row in main_rows.items():
        if k in deleted:
            applied_del += 1
            continue
        if k in edited:
            row = sorted(edited[k], key=lambda p: p[0])[0][1]
            applied_edit += 1
        result[k] = row
    new_keys = [k for k in added if k not in result and k not in deleted]
    new_keys.sort(key=lambda k: ((added[k][0].get("state") or ""), (added[k][0].get("city") or ""), k))

    burned_skipped = []
    if not args.keep_burned:
        kept = []
        for k in new_keys:
            row, branches = added[k]
            if burned(row, " ".join(branches).lower()):
                burned_skipped.append(k)
            else:
                kept.append(k)
        new_keys = kept

    for k in new_keys:
        result[k] = added[k][0]

    print("")
    print("  3-way merge result")
    print("  ------------------")
    print("  rows deleted   : %5d  (main rows a branch genuinely removed)" % applied_del)
    print("  rows edited    : %5d  (field corrections)" % applied_edit)
    print("  rows added     : %5d  (new properties)" % len(new_keys))
    if burned_skipped:
        print("  burned-class new rows skipped: %d  (use --keep-burned to import)" % len(burned_skipped))
    print("  conflicts      : %5d  (both sides changed; row kept as main's version)" % len(conflicts))
    print("  deleted+edited elsewhere (deletion won): %d" % len(set(deleted) & (set(conflicted) | set(edited))))
    print("  %d -> %d rows" % (len(main_rows), len(result)))

    # Serialize with the repo's conventions: UTF-8 BOM, quoted, LF in the index.
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n",
                       extrasaction="ignore")
    w.writeheader()
    for row in result.values():
        w.writerow({f: row.get(f, "") for f in fields})
    out_text = "\ufeff" + buf.getvalue()

    report = {
        "main": main_sha,
        "branches_ahead": len(ahead),
        "main_rows": len(main_rows),
        "result_rows": len(result),
        "deleted": sorted(deleted),
        "edited": sorted(edited),
        "added": sorted(added),
        "conflicts": sorted(conflicts),
        "conflicted": sorted(conflicted),
        "burned_skipped": sorted(burned_skipped),
        "added_source": {k: sorted(v[1]) for k, v in added.items()},
        "deleted_source": {k: sorted(v) for k, v in deleted.items()},
    }
    rp = os.path.join(REPO, args.report)
    os.makedirs(os.path.dirname(rp), exist_ok=True)
    with open(rp, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1)
    print("  report: %s" % rp)

    if args.write:
        path = os.path.join(REPO, args.out)
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(out_text)
        print("  wrote: %s (%d bytes)" % (path, len(out_text.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())

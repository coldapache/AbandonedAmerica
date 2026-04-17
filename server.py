"""Local dev server for Abandoned America with CSV write support."""

import csv
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

CSV_PATH = "Abandoned America - Abandoned or Unused Properties.csv"


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/api/confirm":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            address = body.get("address", "")

            if not address:
                self._json_response(400, {"error": "address required"})
                return

            # Read CSV, update the matching row, write back
            rows = []
            headers = []
            found = False
            with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                if "human_confirmed" not in headers:
                    headers = list(headers) + ["human_confirmed"]
                for row in reader:
                    if row["address"] == address:
                        row["human_confirmed"] = "HUMAN CONFIRMED"
                        found = True
                    rows.append(row)

            if not found:
                self._json_response(404, {"error": "property not found"})
                return

            with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=headers, quoting=csv.QUOTE_ALL)
                writer.writeheader()
                writer.writerows(rows)

            self._json_response(200, {"ok": True, "address": address})
        else:
            self._json_response(404, {"error": "not found"})

    def _json_response(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(("127.0.0.1", 8080), Handler)
    print("Serving at http://localhost:8080")
    server.serve_forever()

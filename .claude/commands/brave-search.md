# Brave Search

Search the web using the Brave Search API. Returns relevant results for any query.

## Input

The user will provide a search query as the argument.

## Usage

```
/brave-search abandoned properties Portsmouth VA
```

## Steps

### 1. Build the API request

Use the Brave Web Search API:

```bash
curl -s "https://api.search.brave.com/res/v1/web/search?q=QUERY&count=10" \
  -H "Accept: application/json" \
  -H "Accept-Encoding: gzip" \
  -H "X-Subscription-Token: $BRAVE_SEARCH_API_KEY"
```

Replace `QUERY` with the URL-encoded search query from the user's input.

### 2. Parse and display results

Extract from the JSON response:
- `web.results[]` — the main web results
- For each result, show: `title`, `url`, and `description`

### 3. Present results

Format the output as a clean numbered list:

```
1. **Title of Result**
   URL: https://example.com/page
   Description text here...

2. **Another Result**
   URL: https://example.com/other
   More description...
```

If the user asked a question, summarize the key findings from the results. If they're looking for data sources, highlight the most promising URLs.

# UK Procurement Bid/No-Bid Service
Deterministic, reproducible scoring over the live UK Contracts Finder OCDS feed. `generate.py` retrieves the feed and applies the versioned `deterministic-v1` heuristic; no model randomness is involved. Schema: `schema.json`; pinned example: `sample-output.json`.

Run: `python generate.py`. Source: https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?limit=10

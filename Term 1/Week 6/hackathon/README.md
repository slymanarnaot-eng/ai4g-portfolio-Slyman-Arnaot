# Rail Pulse — notebook-only project

Based on **Hackathon 6 — Live Pulse — Desk Research**. SDG 9: railway infrastructure reliability. Intended user: NS/ProRail passenger communications or service-quality analyst. The project observes public social posts, not all passengers.

## Notebooks (run in order)
1. `01_live_collector.ipynb` — install dependencies, load `cardiffnlp/twitter-xlm-roberta-base-sentiment` locally, continuously stream Bluesky Jetstream, filter Dutch railway / public transport posts, store predictions in `rail_pulse.sqlite3`. Keep notebook kernel awake **at least 48 hours**.
2. `02_live_dashboard.ipynb` — open in a second notebook kernel from the same directory; inspect rolling 48-hour volume, hourly sentiment and underlying posts; use Refresh (or optional automatic refresh).
3. `03_evaluation.ipynb` — after collecting 50+ items, generate a blind human labelling CSV, label 50 manually, compare with `cardiffnlp/twitter-roberta-base-sentiment-latest`, and explain three errors.

No `.py` scripts are required. Generated `.sqlite3` and `.csv` files are the collected evidence, not included before actual collection. Do not shut down or suspend the machine during collection; background notebook thread stops when the kernel dies. Monitor heartbeat and session timestamps. A first/last timestamp difference is not proof of uninterrupted uptime.

## Scope and integrity
Keyword filters are heuristics and can include news, bot announcements or unrelated items. The broader public transport category is **not** equivalent to railway disruption reactions. Report counts for each category and manually audit relevance. Never invent 300 items. Bluesky stream has no arbitrary keyword server-side filter, so matching happens locally. Data collected while the app is offline may be missed.

## Model choices
Primary: CardiffNLP Twitter XLM-RoBERTa sentiment (multilingual, social-media-oriented, three labels). Comparison: CardiffNLP Twitter RoBERTa sentiment latest (English-oriented, three labels). Read their model cards for training sets and current licence details before submitting: https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment and https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest. Model predictions run locally, no chat API.

## Ethics and limitations
Social posters are not representative of Dutch passengers; Dutch dialect, sarcasm, negation, bots and operational alerts may distort sentiment. The collector hashes post URIs and does not store handles or profile data. Store only necessary text and timestamps, follow Bluesky's terms and relevant data protection rules, show post counts next to trends, and require human review before taking action. Sentiment does not identify the engineering cause of an incident.

## Deliverables still requiring your work
48+ hours of actual collection; 300+ real relevant posts; `rail_pulse.sqlite3`; human-labelled 50-item CSV; comparison CSV and three explained failures; live dashboard demonstration; verified model card/licence summary and terms review. Notebook code is a starter implementation and has not been live-tested end to end here.

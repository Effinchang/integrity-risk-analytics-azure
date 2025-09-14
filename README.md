# integrity-risk-analytics-azure
Cloud-native risk scoring (FastAPI + Streamlit) with Azure-ready CI/CD and Responsible AI docs.
**Keywords:** Azure, FastAPI, Streamlit, XGBoost, SHAP, CI/CD, DevSecOps, Responsible AI, DataOps
## Architecture
- app/fastapi_app.py — `/score`, `/explain`
- ui/streamlit_app.py — upload CSV → scores + explanations
- Azure Web App ready; secrets via env vars/Key Vault
- GitHub Actions → test → scan → deploy
## Quickstart
```bash
pip install -r requirements.txt
uvicorn app.fastapi_app:app --host 0.0.0.0 --port 8000 &
streamlit run ui/streamlit_app.py --server.address 0.0.0.0 --server.port 8501
## API

Health
```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/score \
  -H "Content-Type: application/json" \
  -d '{"amount":4800,"tenure":36,"prior_flags":1}'

Windows tip: open two terminals—run `uvicorn ...` in one, `streamlit ...` in the other (since `&` backgrounding behaves differently).

### next steps
- Pin this repo on your profile (Customize your pins → select it).
- Create the other two repos the same way, including CI and topics:
  - `procurement-pattern-detection` → topics: `procurement graph-database neo4j pattern-detection anomaly-detection data-quality`
  - `genai-structured-extraction` → topics: `generative-ai prompt-engineering structured-extraction nlp evaluation responsible-ai`

Drop me those two URLs and I’ll update your CV + cover letter with the explicit links immediately.
::contentReference[oaicite:0]{index=0}






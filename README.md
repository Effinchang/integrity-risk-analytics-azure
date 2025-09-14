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

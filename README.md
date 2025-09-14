# integrity-risk-analytics-azure
Cloud-native risk scoring (FastAPI + Streamlit) with Azure-ready CI/CD and Responsible AI docs.
**Keywords:** Azure, FastAPI, Streamlit, XGBoost, SHAP, CI/CD, DevSecOps, Responsible AI, DataOps
## Architecture
- app/fastapi_app.py — `/score`, `/explain`
- ui/streamlit_app.py — upload CSV → scores + explanations
- Azure Web App ready; secrets via env vars/Key Vault
- GitHub Actions → test → scan → deploy
## Quickstart
pip install -r requirements.txt
uvicorn app.fastapi_app:app --reload
streamlit run ui/streamlit_app.py

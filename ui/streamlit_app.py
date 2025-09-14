import streamlit as st, pandas as pd, requests
st.title("Integrity Risk Analytics — Demo")
file = st.file_uploader("CSV with columns: amount, tenure, prior_flags", type=["csv"])
api = st.text_input("API base", "http://127.0.0.1:8000")
if file:
    df = pd.read_csv(file)
    scores=[]
    for _, r in df.iterrows():
        payload={"amount":float(r['amount']),"tenure":int(r['tenure']),"prior_flags":int(r['prior_flags'])}
        try:
            out=requests.post(f"{api}/score", json=payload, timeout=5).json()
            scores.append(out.get("risk_score"))
        except Exception:
            scores.append(None)
    st.dataframe(df.assign(risk_score=scores))

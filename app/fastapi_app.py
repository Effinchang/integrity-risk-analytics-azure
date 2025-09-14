from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Integrity Risk Scoring API")
class Item(BaseModel):
    amount: float
    tenure: int
    prior_flags: int

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/score")
def score(item: Item):
    s = 0.2*(item.amount/10000)+0.5*(item.prior_flags)+0.3*(item.tenure/60)
    return {"risk_score": float(np.clip(s,0,1))}

@app.post("/explain")
def explain(item: Item):
    return {"top_factors":["prior_flags","amount","tenure"]}

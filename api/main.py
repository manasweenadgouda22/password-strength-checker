from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passcheck import evaluate_password

app = FastAPI(title="Password Strength Checker API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EvalReq(BaseModel):
    password: str

@app.post("/evaluate")
def evaluate(req: EvalReq):
    return evaluate_password(req.password)

@app.get("/healthz")
def healthz():
    return {"ok": True}

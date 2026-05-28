from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import StudentInput, PredictionOutput
from app.model import model
import pandas as pd
import os

app = FastAPI()

# Allow all origins in production (Render frontend URL is set via env var)
allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    allowed_origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Encoding maps matching training data
ENCODINGS = {
    "school":     {"GP": 0, "MS": 1},
    "sex":        {"F": 0, "M": 1},
    "address":    {"R": 0, "U": 1},
    "famsize":    {"GT3": 0, "LE3": 1},
    "Pstatus":    {"A": 0, "T": 1},
    "Mjob":       {"at_home": 0, "health": 1, "other": 2, "services": 3, "teacher": 4},
    "Fjob":       {"at_home": 0, "health": 1, "other": 2, "services": 3, "teacher": 4},
    "reason":     {"course": 0, "home": 1, "other": 2, "reputation": 3},
    "guardian":   {"father": 0, "mother": 1, "other": 2},
    "schoolsup":  {"no": 0, "yes": 1},
    "famsup":     {"no": 0, "yes": 1},
    "paid":       {"no": 0, "yes": 1},
    "activities": {"no": 0, "yes": 1},
    "nursery":    {"no": 0, "yes": 1},
    "higher":     {"no": 0, "yes": 1},
    "internet":   {"no": 0, "yes": 1},
    "romantic":   {"no": 0, "yes": 1},
}

def encode_input(data: dict) -> dict:
    encoded = data.copy()
    for field, mapping in ENCODINGS.items():
        raw = encoded.get(field)
        if raw not in mapping:
            raise HTTPException(
                status_code=422,
                detail=f"Invalid value '{raw}' for field '{field}'. Accepted values: {list(mapping.keys())}"
            )
        encoded[field] = mapping[raw]
    return encoded

@app.post("/predict", response_model=PredictionOutput)
def predict(data: StudentInput):
    encoded = encode_input(data.dict())
    input_df = pd.DataFrame([encoded])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df).tolist()[0]
    label = "Pass" if prediction == 1 else "Fail"
    return PredictionOutput(
        prediction=int(prediction),
        prediction_label=label,
        probability=probability
    )

@app.get("/metrics")
def get_metrics():
    return {
        "accuracy": 0.8025,
        "f1_score": 0.8839,
        "precision": 0.8166,
        "recall": 0.9633,
        "note": "Recall for Fail cases is only 23%. The model may not catch all at-risk students. Use predictions as a guide, not a definitive assessment.",
        "class_report": {
            "Fail": {"precision": 0.64, "recall": 0.23, "f1_score": 0.34, "support": 69},
            "Pass": {"precision": 0.82, "recall": 0.96, "f1_score": 0.88, "support": 245}
        },
        "total_support": 314
    }

@app.get("/")
def root():
    return {"status": "ok", "message": "Student Performance Classifier API"}
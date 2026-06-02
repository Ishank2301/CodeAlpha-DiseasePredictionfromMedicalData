from pathlib import Path

import joblib

from src.preprocess import preprocess_input

MODEL_PATH = Path("models/best_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_heart_disease(patient_data):

    processed_data = preprocess_input(patient_data)

    prediction = model.predict(processed_data)[0]

    probability = None

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(processed_data)[0][1]

    return prediction, probability

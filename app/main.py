from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

class Message(BaseModel):
    text: str

app = FastAPI(title="Spam Detection API")

model_path = "app/model/linear_svm_spam_model.joblib"
model = joblib.load(model_path)  # Load the pipeline directly

@app.post("/predict")
def predict(message: Message):
    text = [message.text]
    prediction = model.predict(text)[0]  # Use the pipeline directly
    label = "spam" if prediction == 1 else "ham"
    return {"prediction": label}
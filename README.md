# 📦 Spam Detection FastAPI App

This is a FastAPI-based web app that serves a trained Linear SVM spam detection model.

## 🚀 How to Run

### Option 1: With Docker

```bash
docker build -t spam-api .
docker run -p 8000:8000 spam-api
```

### Option 2: Without Docker

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🧪 Test the API

Send a POST request to `http://localhost:8000/predict` with JSON:

```json
{
  "text": "Congratulations! You've won a free cruise!"
}
```

Response:
```json
{
  "prediction": "spam"
}
```
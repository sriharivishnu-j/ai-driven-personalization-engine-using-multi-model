from fastapi import FastAPI, HTTPException
import logging
from services.ai_service import AIModelService

app = FastAPI()
logging.basicConfig(level=logging.INFO)
ai_service = AIModelService()

@app.get('/')
async def root():
    return {"message": "AI-Driven Personalization Engine"}

@app.get('/predict/{user_id}')
async def predict(user_id: str):
    try:
        prediction = ai_service.predict(user_id)
        return prediction
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")

from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from fastapi import HTTPException, Security
import pandas as pd
import joblib
import os
from dotenv import load_dotenv
from api.models import PropertyFeatures
from utils.logger import get_logger

# Load environment variables from api_keys.env file
load_dotenv(dotenv_path="/app/api_keys.env")

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = os.getenv("API_KEY_NAME")

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

model = joblib.load('/app/model/model.joblib')

logger = get_logger(__name__)

async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
):
    if api_key_query == API_KEY or api_key_header == API_KEY:
        return API_KEY
    else:
        logger.warning("Invalid API key provided.")
        raise HTTPException(status_code=403, detail="Could not validate credentials")

def predict_property_value(features: PropertyFeatures):
    logger.info(f"Received prediction request: {features.dict()}")
    data = pd.DataFrame([features.dict()])
    prediction = model.predict(data)
    logger.info(f"Prediction result: {prediction[0]}")
    return {"prediction": prediction[0]}

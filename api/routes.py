from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.api_key import APIKey
from api.controller import predict_property_value, get_api_key
from api.models import PropertyFeatures

router = APIRouter()

@router.post("/predict")
def predict(features: PropertyFeatures, api_key: APIKey = Depends(get_api_key)):
    try:
        return predict_property_value(features)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

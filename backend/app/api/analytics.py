from fastapi import APIRouter
from app.services.featureEngineering import featureEngineeringService

router = APIRouter(prefix = "/analytics", tags = ["Analytics"])

featureService = featureEngineeringService()

@router.get("/{ticker}/features")

def get_some(ticker: str):
    return featureService.get_Features(ticker)
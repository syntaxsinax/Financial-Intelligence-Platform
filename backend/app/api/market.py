from fastapi import APIRouter
from app.services.marketData import MarketDataService

router = APIRouter(prefix = "/market", tags=["market"])
market_service = MarketDataService()


@router.get("/test")
def market_test:
    return market_service.get_status()



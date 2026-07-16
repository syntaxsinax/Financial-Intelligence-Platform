from fastapi import APIRouter
from app.services.marketData import marketDataService

router = APIRouter(prefix = "/market", tags=["market"])
market_service = marketDataService()


@router.get("/test")
def market_test():
    return market_service.get_status()

@router.get("/{ticker}")
def get_marketData(ticker: str):
    return market_service.get_stockinfo(ticker)



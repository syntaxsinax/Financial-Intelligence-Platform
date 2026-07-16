from pydantic import BaseModel


class StockInfo(BaseModel):
    ticker: str
    company_name: str | None
    current_price: float | None
    currency: str | None
    exchange: str | None

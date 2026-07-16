import yfinance as yf

class marketDataService:

    def get_status(self):
        return {
            "Service": "MarketDataService",
            "Status": "Operational"
        }

    def get_stockinfo(self, ticker: str):
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "ticker": ticker.uppeer(),
            "company_name": info.get(longName),
            "current_price": info.get(currentPrice),
            "currency": info.get("currency"),
            "exchange": info.get("exchange")
        }

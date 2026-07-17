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
            "ticker": ticker.upper(),
            "company_name": info.get("longName"),
            "current_price": info.get("currentPrice"),
            "currency": info.get("currency"),
            "exchange": info.get("exchange")
        }
    
    def get_stockhistory(self, ticker: str, period: str = "1mo"):
        stock = yf.Ticker(ticker)
        history = stock.history(period=period)
        record = []

        for date, row in history.iterrows():
            record.append({
                "date": date.strftime("%Y-%m-%d"),
                "open": float(row["Open"]),
                "high": float(row["High"]),
                "low": float(row["Low"]),
                "close": float(row["Close"]),
                "volume": int(row["Volume"])

            })
        return record


    def get_historyDataframe(self, ticker: str, period: str = "6mo"):
        stock = yf.Ticker(ticker)
        return stock.history(period=period)



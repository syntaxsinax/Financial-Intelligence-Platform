from app.services.marketData import marketDataService


class featureEngineeringService:
    def __init__(self):
        self.marketService = marketDataService()

    def get_Features(self, ticker: str):
        df = self.marketService.get_historyDataframe(ticker)

        df["Daily_Return"] = df["Close"].pct_change()
        df["SMA_20"] = df["Close"].rolling(20).mean()
        df["EMA_20"] = df["Close"].ewm(span=20).mean()
        df["Volatility"] = df["Daily_Return"].rolling(20).std()

        latest = df.iloc[-1]

        return {
            "ticker": ticker.upper(),
            "lastest_close": round(float(latest["Close"]), 2),
            "daily_return": round(float(latest["Daily_Return"]), 5),
            "SMA_20": round(float(latest["SMA_20"]), 2),
            "EMA_20": round(float(latest["EMA_20"]), 2),
            "volatility": round(float(latest["Volatility"]), 5)

        }

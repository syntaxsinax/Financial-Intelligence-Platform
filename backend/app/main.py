from fastapi import FastAPI
from app.api.root import router as root_router
from app.api.market import router as market_router

app = FastAPI()
app.include_router(root_router)
app.include_router(market_router)

@app.get("/")
def root():
    return {
        "project": "Financial Intelligence Platform",
        "status": "Running"
    }
   
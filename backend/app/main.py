from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "project": "Financial Intelligence Platform",
        "status": "Running"
    }
   
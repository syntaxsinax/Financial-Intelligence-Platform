from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "project": "Financial Intelligence Platform",
        "status": "running"
    }
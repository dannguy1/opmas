from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Welcome to the OPMAS Management API v1"}


@router.get("/health")
async def health_check():
    return {"status": "healthy"}

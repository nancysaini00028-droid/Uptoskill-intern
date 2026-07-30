from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints.certificates import router as certificates_router

app = FastAPI(
    title=settings.PROJECT_NAME
)
app.include_router(certificates_router, prefix="/certificates", tags=["Certificates"])

@app.get("/")
async def root():
    return {
        "message": "InternOps AI Service is running!"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "ok"
    }

print("main.py loaded")    
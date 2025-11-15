from fastapi import FastAPI
from app.routes.crypto import router as crypto_router
from app.utils.errors import setup_error_handlers

app = FastAPI(title="MCP Crypto Server")

app.include_router(crypto_router, prefix="/api")
setup_error_handlers(app)

@app.get("/")
def root():
    return {"message": "MCP Server is running"}
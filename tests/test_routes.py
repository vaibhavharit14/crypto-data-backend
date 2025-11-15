from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "MCP Server is running"}

def test_realtime_route():
    response = client.get("/api/realtime?exchange=binance&symbol=BTC/USDT")
    assert response.status_code == 200
    assert "price" in response.json() or "error" in response.json()

def test_historical_route():
    response = client.get("/api/historical?exchange=binance&symbol=BTC/USDT&timeframe=1h&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list) or "error" in response.json()
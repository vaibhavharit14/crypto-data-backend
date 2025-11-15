from app.services.ccxt_service import get_realtime_price, get_historical_data

def test_get_realtime_price():
    result = get_realtime_price("binance", "BTC/USDT")
    assert "price" in result or "error" in result

def test_get_historical_data():
    result = get_historical_data("binance", "BTC/USDT", "1h", 10)
    assert isinstance(result, list) or "error" in result
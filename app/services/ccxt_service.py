import ccxt

def get_realtime_price(exchange_name: str, symbol: str):
    try:
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class()
        ticker = exchange.fetch_ticker(symbol)
        return {
            "symbol": symbol,
            "price": ticker["last"],
            "timestamp": ticker["timestamp"]
        }
    except Exception as e:
        return {"error": str(e)}

def get_historical_data(exchange_name: str, symbol: str, timeframe: str = "1h", limit: int = 100):
    try:
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class()
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        return [
            {
                "timestamp": candle[0],
                "open": candle[1],
                "high": candle[2],
                "low": candle[3],
                "close": candle[4],
                "volume": candle[5]
            }
            for candle in ohlcv
        ]
    except Exception as e:
        return {"error": str(e)}
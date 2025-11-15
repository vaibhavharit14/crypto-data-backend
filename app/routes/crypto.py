from fastapi import APIRouter, Query
from app.services.ccxt_service import get_realtime_price, get_historical_data

router = APIRouter()

@router.get("/realtime")
def fetch_realtime_price(
    exchange: str = Query(..., examples={"binance": {"value": "binance"}}),
    symbol: str = Query(..., examples={"BTC/USDT": {"value": "BTC/USDT"}})
):
    return get_realtime_price(exchange, symbol)

@router.get("/historical")
def fetch_historical_data(
    exchange: str = Query(..., examples={"binance": {"value": "binance"}}),
    symbol: str = Query(..., examples={"BTC/USDT": {"value": "BTC/USDT"}}),
    timeframe: str = Query("1h", examples={"1h": {"value": "1h"}}),
    limit: int = Query(100, examples={"100": {"value": 100}})
):
    return get_historical_data(exchange, symbol, timeframe, limit)
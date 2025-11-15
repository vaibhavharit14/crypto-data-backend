from functools import lru_cache

@lru_cache(maxsize=128)
def cached_price(exchange: str, symbol: str):
    return f"{exchange}-{symbol}"
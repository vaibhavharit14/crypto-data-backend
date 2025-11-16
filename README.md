# 📘 MCP Crypto Server – FastAPI Backend

A modular, production-ready backend for real-time and historical cryptocurrency data using FastAPI and `ccxt`. Built for speed, scalability, and recruiter polish.

---

## 🚀 Live Deployment

- **Render URL:** [https://crypto-data-backend.onrender.com](https://crypto-data-backend.onrender.com)  
- **Swagger Docs:** [https://crypto-data-backend.onrender.com/docs](https://crypto-data-backend.onrender.com/docs)

---

## 🧱 Tech Stack

- **FastAPI** – High-performance Python web framework  
- **ccxt** – Unified crypto exchange API  
- **Uvicorn** – ASGI server for FastAPI  
- **Pydantic** – Data validation and schema generation  
- **Render** – Cloud deployment platform

---

## 📁 Folder Structure
crypto-data-backend/ ├── app/ │   ├── routes/          # API routes (e.g. crypto.py) │   ├── services/        # Business logic (ccxt integration) │   ├── utils/           # Error handling, config, cache ├── tests/               # Unit tests ├── main.py              # FastAPI entry point ├── requirements.txt     # Dependencies ├── .env.example         # Environment config template

---

## 📡 API Endpoints

### `GET /api/realtime`

Fetches real-time price data.

**Query Params:**
- `exchange`: e.g. `binance`
- `symbol`: e.g. `BTC/USDT`

**Example:**
GET /api/realtime?exchange=binance&symbol=BTC/USDT

---

### `GET /api/historical`

Fetches historical OHLCV data.

**Query Params:**
- `exchange`: e.g. `binance`
- `symbol`: e.g. `BTC/USDT`
- `timeframe`: default `1h`
- `limit`: default `100`

**Example:**
GET /api/historical?exchange=binance&symbol=BTC/USDT&timeframe=1h&limit=100

 ---







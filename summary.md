
---

### 📄 `summary.md`

```markdown
# Project Summary: Binance Price Capture

## ✅ Goal

To continuously capture real-time prices of BTC/ETH from Binance and store them in a PostgreSQL database for analytics.

---

## ⚙️ Main Components

### 1. PostgreSQL Table Setup

Table `prices` created with:
- `symbol` (e.g., BTCUSDT)
- `price` (live price)
- `timestamp` (insertion time)

### 2. Data Ingestion (main.py)

- Connects to Binance via WebSocket
- Filters BTC and ETH prices
- Inserts new rows into PostgreSQL every second (or faster)

### 3. Queries (queries.py)

- `get_latest_price`: latest real-time price
- `get_price_at_time`: price at specific timestamp
- `get_high_low`: highest and lowest price in last 1 minute

---

## 🔍 Query Example Outputs

Latest BTC: ('BTCUSDT', 106512.09, 2025-07-01 17:23:36+05:30)
Price at time: ('BTCUSDT', 106512.09, 2025-07-01 17:22:36+05:30)
High/Low: (106522.74, 106512.08)


---

## 📊 Access via pgAdmin

Use "View/Edit Data > All Rows" to browse data or SQL to filter.

---

## ✅ Outcome

- Functional pipeline to stream and store live crypto data
- Queryable historical database
- Realtime insights for potential trading use cases

---

## 🚀 Future Improvements

- Store OHLCV (open-high-low-close-volume)
- Add technical indicators
- Build Streamlit dashboard for traders

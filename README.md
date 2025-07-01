# Binance-WebSocket-Price-Precision-Capture-BTC-ETH-
Consume live price updates from Binance WebSocket and persist accurately
# Binance Price Capture with PostgreSQL

## 📌 Project Overview

This project captures live cryptocurrency prices (BTCUSDT and ETHUSDT) from the Binance WebSocket API and stores them in a PostgreSQL database. It also includes a querying tool to fetch real-time analytics like latest price, price at specific timestamp, and high/low in the last minute.

---

## 🔧 Tech Stack

- Python
- PostgreSQL
- pgAdmin
- Binance WebSocket API

---

## 📁 Folder Structure

binance_price_capture/
├── db.py # DB connection + insert logic
├── main.py # WebSocket stream to collect price data
├── queries.py # Query logic for latest price, high/low etc.
├── schema.sql # SQL script to create the prices table
├── README.md # Project documentation
├── summary.md # Execution summary


---

## ⚙️ Setup Instructions

### 1. Clone the Repo
git clone https://github.com/karthikeyapranav/Binance-WebSocket-Price-Precision-Capture-BTC-ETH-.git

### 2. Create the PostgreSQL Table
Run:

psql -U postgres -d crypto -p 5433 -f schema.sql
This creates the prices table.

### 3. Update DB Credentials
In both db.py and queries.py, update:

conn = psycopg2.connect(
    dbname="crypto",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5433"
)
🚀 Running the Scripts
🔹 Start WebSocket Data Capture
python main.py
This will stream live prices of BTC and ETH and insert them into PostgreSQL.

🔹 Query Data from Database


python queries.py
It shows:

Latest price

Price at specific time (1 minute ago)

High/Low in the last 1 minute

📊 Viewing in pgAdmin
Open pgAdmin

Navigate to your crypto database > prices table

Right-click → View/Edit Data → All Rows

Or run SQL:


SELECT * FROM prices WHERE symbol = 'BTCUSDT';
🧠 Use Cases
Realtime price monitoring

Building crypto dashboards

Strategy testing with live price feed

✅ Next Steps
Add support for more pairs

Set up a dashboard (e.g., Streamlit or Grafana)

Implement alerts when price crosses thresholds

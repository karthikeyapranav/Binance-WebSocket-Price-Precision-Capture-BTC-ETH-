#  Project Summary: Binance Live Price Capture & Analytics

##  Core Goal

The central aim of this project is to build a robust and precise pipeline for **continuously capturing real-time cryptocurrency prices** (specifically BTCUSDT and ETHUSDT) directly from the Binance WebSocket API and reliably storing them in a **PostgreSQL database** for immediate and historical analytics.

---

##  Main Components & Their Functionality

This project is structured around several key components, each playing a vital role in the data flow:

### 1. PostgreSQL Database Table (`schema.sql`)

* **Purpose:** To serve as a high-precision, persistent storage for every incoming price tick.
* **Table Structure (`prices`):**
    * `id`: Unique identifier for each price record (Primary Key).
    * `symbol`: The trading pair (e.g., `BTCUSDT`, `ETHUSDT`). This uses `VARCHAR` for flexible symbol names.
    * `price`: The actual trade price. This is stored as `NUMERIC(20, 10)` to ensure high precision, crucial for financial data where tiny fractions matter.
    * `timestamp`: The exact time the price was recorded (insertion time). Stored as `TIMESTAMP WITH TIME ZONE` for accurate timekeeping across different time zones.

### 2. Data Ingestion Stream (`main.py`)

* **Purpose:** To act as the real-time data "producer," connecting to Binance and feeding data into the database.
* **Mechanism:**
    * Establishes a **live WebSocket connection** with Binance's public market data streams.
    * **Filters** incoming messages to specifically capture `trade` events for BTCUSDT and ETHUSDT.
    * **Parses** the JSON messages to extract the `symbol`, `price`, and `timestamp` of each trade.
    * **Inserts** each new trade record into the `prices` table in PostgreSQL. This happens almost instantaneously as new trades occur on Binance, ensuring near real-time data availability.

### 3. Data Querying & Analytics (`queries.py`)

* **Purpose:** To demonstrate how to retrieve and analyze the captured price data from PostgreSQL.
* **Key Functions:**
    * `get_latest_price(symbol)`: Fetches the most recent price and its timestamp for a given trading pair. This is vital for showing current market conditions.
    * `get_price_at_time(symbol, target_timestamp)`: Retrieves the price of a symbol at or closest to a specified historical timestamp. This allows for historical point-in-time analysis.
    * `get_high_low(symbol, interval_minutes)`: Calculates the highest and lowest prices recorded for a symbol within a specified recent time window (e.g., the last 1, 5, or 60 minutes). This helps in understanding recent volatility and range.

---

##  Example Query Outputs

When you run the `queries.py` script, you'll see output similar to this (values will vary based on live market data and execution time):

Latest Price for BTCUSDT: ('BTCUSDT', 106512.09, '2025-07-08 22:05:30.123456+05:30')
Price for BTCUSDT at 1 minute ago: ('BTCUSDT', 106500.50, '2025-07-08 22:04:30.987654+05:30')
High/Low for BTCUSDT in last 1 minute: High=106550.00, Low=106490.10

Latest Price for ETHUSDT: ('ETHUSDT', 3500.25, '2025-07-08 22:05:30.001234+05:30')
Price for ETHUSDT at 1 minute ago: ('ETHUSDT', 3495.70, '2025-07-08 22:04:30.567890+05:30')
High/Low for ETHUSDT in last 1 minute: High=3505.00, Low=3490.00

*Note: Timestamps and prices will reflect the actual data captured during your run.*

---

##  Visualizing Data with pgAdmin

For a more intuitive way to explore the captured data, `pgAdmin` is an excellent tool:

1.  Connect to your `crypto` database within `pgAdmin`.
2.  Navigate to the `prices` table (`Databases` > `crypto` > `Schemas` > `public` > `Tables` > `prices`).
3.  Right-click the `prices` table and select "View/Edit Data" -> "All Rows" to see all captured records.
4.  You can also open a Query Tool and run custom SQL queries to filter, sort, or aggregate the data as needed, e.g., `SELECT * FROM prices WHERE symbol = 'BTCUSDT' ORDER BY timestamp DESC LIMIT 100;`.

---

##  Project Outcome

This project successfully establishes a **fully functional and precise pipeline** that:

* **Streams and stores live cryptocurrency data** directly from a major exchange (Binance) into a robust database.
* Provides a **queryable historical database** that can be used for both immediate analysis and long-term research.
* Enables the extraction of **real-time insights**, laying a strong foundation for various financial applications and potential trading use cases.

---

##  Future Enhancements & Next Steps

This project is a solid starting point and can be significantly expanded:

* **Store OHLCV Data:** Instead of just raw trades, aggregate data into Open, High, Low, Close, and Volume (OHLCV) bars (e.g., 1-minute, 5-minute candles). This is a standard format for technical analysis.
* **Add Technical Indicators:** Integrate libraries to calculate popular technical indicators (e.g., Moving Averages, RSI, MACD) directly from the captured data.
* **Build a Live Dashboard:** Develop a user-friendly web interface (e.g., using Streamlit, Dash, or a custom web framework) to visualize live price charts, indicators, and real-time alerts for traders.
* **Implement Alerting System:** Set up automated alerts (email, Telegram, etc.) when specific price conditions are met (e.g., price crosses a threshold, significant volume spike).
* **Enhance Data Resilience:** Implement robust error handling, automatic WebSocket reconnection logic, and potentially a message queue (like Kafka) between the WebSocket and DB for higher fault tolerance in production environments.
* **Containerization:** Use Docker and Docker Compose to bundle the Python scripts and PostgreS

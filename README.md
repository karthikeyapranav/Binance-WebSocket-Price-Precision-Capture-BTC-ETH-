# 📈 Binance WebSocket Price Precision Capture: BTC & ETH

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-316192.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Binance API](https://img.shields.io/badge/Binance%20API-WebSocket-FCD535.svg?logo=binance&logoColor=black)](https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project provides a robust solution for capturing real-time cryptocurrency price updates directly from the **Binance WebSocket API** and persisting them with high precision into a **PostgreSQL database**. Beyond just data collection, it includes a powerful querying tool to extract immediate insights, such as the latest price, historical prices at specific timestamps, and high/low values within a given timeframe.

It's an essential foundation for anyone looking to build real-time crypto analytics dashboards, trading bots, or historical data analysis platforms.

---

## 📌 Project Overview

The core idea is to create a reliable and accurate pipeline for live market data. By consuming data directly from Binance's low-latency WebSocket, we ensure that every price tick is captured. Storing this data in PostgreSQL allows for efficient querying and analysis, enabling both real-time monitoring and historical backtesting.

### Key Capabilities:

* **Live Price Ingestion:** Connects to Binance's WebSocket to stream real-time price updates for BTCUSDT and ETHUSDT.
* **High-Precision Storage:** Persists price data, including precise timestamps and values, into a PostgreSQL database.
* **Real-time Analytics:** Offers a command-line tool to query the database for immediate insights, such as:
    * The absolute latest recorded price for a symbol.
    * The price of a symbol at any given historical timestamp.
    * The highest and lowest prices within a specified recent time window (e.g., last minute).

---

## 🔧 Tech Stack

This project is built using a straightforward yet powerful combination of technologies:

* **Python:** The primary programming language used for WebSocket communication, data processing, and database interaction.
* **PostgreSQL:** A powerful, open-source relational database known for its reliability, data integrity, and advanced querying capabilities. Ideal for storing time-series data like price ticks.
* **pgAdmin:** A popular open-source administration and development platform for PostgreSQL, used for database management and visual data inspection.
* **Binance WebSocket API:** Provides a direct, low-latency stream of market data, including real-time price updates.

---

## 📁 Folder Structure

The project is organized into logical components for clarity and maintainability:
binance_price_capture/
├── db.py               # Handles PostgreSQL database connection and data insertion logic.
├── main.py             # The core script for establishing WebSocket connection and collecting live price data.
├── queries.py          # Contains functions and logic for querying the collected price data from the database.
├── schema.sql          # SQL script to define and create the 'prices' table in PostgreSQL.
├── README.md           # This comprehensive project documentation.
└── summary.md          # A brief, high-level summary of the project.

---

## ⚙️ Setup Instructions

Follow these steps to get the Binance price capture system up and running on your local machine.

### Prerequisites

* **Python 3.9+:** Make sure Python is installed on your system.
* **PostgreSQL:** Install PostgreSQL. You can use a local installation or a Docker container.
* **pgAdmin (Optional but Recommended):** For easy database management and visualization.

### Step-by-Step Setup

1.  **Clone the Repository:**
    Start by cloning the project repository to your local machine:
    ```bash
    git clone [https://github.com/karthikeyapranav/Binance-WebSocket-Price-Precision-Capture-BTC-ETH-.git](https://github.com/karthikeyapranav/Binance-WebSocket-Price-Precision-Capture-BTC-ETH-.git)
    cd Binance-WebSocket-Price-Precision-Capture-BTC-ETH-
    ```

2.  **Create PostgreSQL Database and User (if needed):**
    Before creating the table, ensure you have a PostgreSQL database (e.g., `crypto`) and a user (e.g., `postgres` with a password) configured. If you're new to PostgreSQL, you might need to create these.

    **Example (using `psql`):**
    ```sql
    CREATE DATABASE crypto;
    CREATE USER postgres WITH PASSWORD 'your_secure_password';
    GRANT ALL PRIVILEGES ON DATABASE crypto TO postgres;
    ```
    *Remember to replace `'your_secure_password'` with a strong password.*

3.  **Create the `prices` Table:**
    Execute the `schema.sql` script to create the necessary `prices` table in your PostgreSQL database. This table is designed to store the captured cryptocurrency prices with high precision.

    ```bash
    # Replace 'your_password' with your PostgreSQL user's password
    psql -U postgres -d crypto -p 5433 -f schema.sql
    ```
    * `-U postgres`: Specifies the PostgreSQL user.
    * `-d crypto`: Connects to the `crypto` database.
    * `-p 5433`: Specifies the port (default is 5432, but 5433 is used in the example).
    * `-f schema.sql`: Executes the SQL commands from `schema.sql`.

4.  **Update Database Credentials:**
    Open `db.py` and `queries.py` and update the `psycopg2.connect` parameters with your actual PostgreSQL database credentials.

    ```python
    # Example snippet from db.py and queries.py
    conn = psycopg2.connect(
        dbname="crypto",
        user="postgres",
        password="your_password", # <--- UPDATE THIS
        host="localhost",
        port="5433"              # <--- UPDATE THIS if your port is different
    )
    ```
    *Ensure the `password` and `port` match your PostgreSQL setup.*

5.  **Install Python Dependencies:**
    Install the required Python libraries:
    ```bash
    pip install websocket-client psycopg2-binary
    ```

---

## 🚀 Running the Scripts

Once the setup is complete, you can start capturing and querying live price data.

### 🔹 1. Start WebSocket Data Capture (Producer)

Run `main.py` to begin streaming live price updates from Binance and inserting them into your PostgreSQL database. This script will run continuously, collecting data.

You will see console output indicating that the WebSocket connection is established and prices are being received and inserted.

Keep this script running in one terminal window to continue capturing data.

🔹 2. Query Data from Database (Consumer/Analytics)
Open a new terminal window and run queries.py. This script demonstrates how to fetch various real-time analytics from your captured data.

python queries.py
The script will execute predefined queries and print the results to the console, showing:

The latest price for BTCUSDT and ETHUSDT.

The price at a specific historical time (e.g., 1 minute ago).

The high and low prices recorded within the last 1 minute.

You can modify queries.py to test different timeframes or symbols.

📊 Viewing Data in pgAdmin (Optional)
For a visual inspection of your captured data and to run custom SQL queries, use pgAdmin:

Open pgAdmin: Launch the pgAdmin application.

Connect to your PostgreSQL server: If you haven't already, add a server connection to your local PostgreSQL instance.

Navigate to your crypto database: Expand "Databases" -> "crypto".

Explore the prices table: Expand "Schemas" -> "public" -> "Tables" -> "prices".

View Data: Right-click on the prices table and select "View/Edit Data" -> "All Rows" to see the captured price entries.

Run Custom SQL: Open a Query Tool (right-click on crypto database -> "Query Tool...") and execute SQL commands like:

SQL

SELECT * FROM prices WHERE symbol = 'BTCUSDT' ORDER BY timestamp DESC LIMIT 10;
SELECT MIN(price), MAX(price) FROM prices WHERE symbol = 'ETHUSDT' AND timestamp >= NOW() - INTERVAL '5 minutes';
🧠 Potential Use Cases
This project serves as a foundational component for various applications in the cryptocurrency domain:

Real-time Price Monitoring: Build dashboards to visualize live price movements.

Algorithmic Trading & Strategy Testing: Feed live and historical data into trading algorithms for backtesting and execution.

Crypto Analytics Dashboards: Create custom analytical tools to track market trends, volatility, and specific asset performance.

Historical Data Analysis: Conduct in-depth research on past market behavior.

Alerting Systems: Implement notifications when prices cross certain thresholds or exhibit unusual patterns.

✅ Next Steps & Enhancements
This project can be extended in many exciting ways:

Support for More Trading Pairs: Easily extend main.py to subscribe to additional cryptocurrency symbols (e.g., XRPUSDT, ADAUSDT).

Build a Dashboard: Integrate with visualization tools like Streamlit, Dash, Grafana, or even a simple Flask/React frontend to create an interactive price dashboard.

Implement Advanced Analytics: Add more complex queries for moving averages, volatility, order book depth, etc.

Threshold-Based Alerts: Develop a system to trigger alerts (e.g., email, SMS, push notification) when prices cross predefined thresholds or significant price changes occur.

Error Handling & Reconnection Logic: Enhance the WebSocket client with robust error handling and automatic reconnection mechanisms to ensure continuous data capture.

Containerization (Docker Compose): Package the PostgreSQL database and Python scripts into Docker containers orchestrated by Docker Compose for even easier setup and deployment.

🤝 Contributing
Contributions, issues, and feature requests are highly welcome! If you have ideas for improvements, new features, or encounter any bugs, please feel free to:

Open an issue: Describe the bug or feature request in detail.

Submit a Pull Request: If you've implemented a solution or a new feature, we'd love to review it!

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
The Binance team for providing comprehensive and reliable WebSocket APIs.

The PostgreSQL community for a robust and versatile database system.

The developers of websocket-client and psycopg2 for their excellent Python libraries.

The open-source community for continuously inspiring and enabling such projects.

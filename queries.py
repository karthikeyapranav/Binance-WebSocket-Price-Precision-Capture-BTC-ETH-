import psycopg2
from datetime import datetime, timedelta
from datetime import datetime, timedelta, timezone

conn = psycopg2.connect(
    dbname="crypto",
    user="postgres",
    password="your password",  # Replace with your actual password
    host="localhost",
    port="5433"
)
cursor = conn.cursor()

def get_latest_price(symbol):
    cursor.execute("""
        SELECT symbol, price, timestamp
        FROM prices
        WHERE symbol = %s
        ORDER BY timestamp DESC
        LIMIT 1;
    """, (symbol,))
    return cursor.fetchone()

def get_price_at_time(symbol, target_time):
    cursor.execute("""
        SELECT symbol, price, timestamp
        FROM prices
        WHERE symbol = %s
        ORDER BY ABS(EXTRACT(EPOCH FROM timestamp - %s))
        LIMIT 1;
    """, (symbol, target_time))
    return cursor.fetchone()

def get_high_low(symbol, start_time, end_time):
    cursor.execute("""
        SELECT MAX(price), MIN(price)
        FROM prices
        WHERE symbol = %s
        AND timestamp BETWEEN %s AND %s;
    """, (symbol, start_time, end_time))
    return cursor.fetchone()

if __name__ == "__main__":
    print(">>")

    symbol = "BTCUSDT" # or "ETHUSDT"

    latest = get_latest_price(symbol)
    print("Latest BTC:", latest)

    # Use current time rounded down to nearest second
    now = datetime.now(timezone.utc).replace(microsecond=0)
    price_at_time = get_price_at_time(symbol, now)
    print("Price at time:", price_at_time)

    one_min_ago = now - timedelta(minutes=1)
    high_low = get_high_low(symbol, one_min_ago, now)
    print("High/Low:", high_low)

    cursor.close()
    conn.close()

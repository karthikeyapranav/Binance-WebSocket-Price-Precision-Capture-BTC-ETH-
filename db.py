import psycopg2
from psycopg2.extras import execute_values

# Connect once
conn = psycopg2.connect(
    dbname="crypto",
    user="postgres",
    password="your password",  # Replace with your actual password
    host="localhost",
    port="5433"
)
conn.autocommit = True

def insert_price(timestamp, symbol, price):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO prices (timestamp, symbol, price)
            VALUES (%s, %s, %s)
        """, (timestamp, symbol, price))

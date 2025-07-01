import asyncio
import json
import websockets
from db import insert_price
from datetime import datetime

async def connect():
    url = "wss://stream.binance.com:9443/ws/btcusdt@trade/ethusdt@trade"
    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            symbol = data['s']
            price = float(data['p'])
            timestamp = datetime.fromtimestamp(data['T'] / 1000.0)

            insert_price(timestamp, symbol, price)
            print(f"{timestamp} | {symbol} | {price}")

asyncio.run(connect())

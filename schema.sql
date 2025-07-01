-- schema.sql

CREATE TABLE IF NOT EXISTS prices (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    symbol TEXT NOT NULL,
    price NUMERIC(18, 8) NOT NULL
);

-- Index for faster queries
CREATE INDEX IF NOT EXISTS idx_symbol_time ON prices(symbol, timestamp);

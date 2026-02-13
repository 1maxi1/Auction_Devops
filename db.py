import os
from flask_sqlalchemy import SQLAlchemy
from typing import Any, Iterable, Optional

import psycopg2
from psycopg2.extras import RealDictCursor

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 
    'postgresql://user:password@postgres:5432/auction_db')
db = SQLAlchemy(app)

class AuctionDB:
    """
    Обёртка над подключением к PostgreSQL.

    Параметры подключения берутся из переменных окружения:
    - DB_NAME (по умолчанию: auction)
    - DB_USER (по умолчанию: postgres)
    - DB_PASSWORD (по умолчанию: пусто)
    - DB_HOST (по умолчанию: localhost)
    - DB_PORT (по умолчанию: 5432)
    """

    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "auction"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            cursor_factory=RealDictCursor,
        )
        self._ensure_schema()

    def _ensure_schema(self) -> None:
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS participants (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                contact_info TEXT,
                notes TEXT
            );
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS auctions (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                starts_at TIMESTAMP NOT NULL,
                description TEXT
            );
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id SERIAL PRIMARY KEY,
                auction_id INTEGER NOT NULL REFERENCES auctions(id) ON DELETE CASCADE,
                seller_id INTEGER NOT NULL REFERENCES participants(id),
                lot_number TEXT NOT NULL,
                title TEXT NOT NULL,
                start_price NUMERIC(12, 2) NOT NULL CHECK (start_price >= 0),
                description TEXT,
                UNIQUE (auction_id, lot_number)
            );
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS sales (
                id SERIAL PRIMARY KEY,
                item_id INTEGER NOT NULL UNIQUE REFERENCES items(id) ON DELETE CASCADE,
                buyer_id INTEGER NOT NULL REFERENCES participants(id),
                sold_price NUMERIC(12, 2) NOT NULL CHECK (sold_price >= 0),
                sold_at TIMESTAMP NOT NULL
            );
            """
        )
        self.conn.commit()

    def query(self, sql: str, params: Iterable[Any] | None = None) -> list[dict]:
        cur = self.conn.cursor()
        cur.execute(sql, params or ())
        rows = cur.fetchall()
        return rows

    def execute(self, sql: str, params: Iterable[Any] | None = None) -> int:
        cur = self.conn.cursor()
        cur.execute(sql, params or ())
        self.conn.commit()
        row_id = cur.fetchone()["id"] if cur.description else None
        return int(row_id) if row_id is not None else 0

    def executemany(self, sql: str, seq_of_params: Iterable[Iterable[Any]]) -> None:
        cur = self.conn.cursor()
        cur.executemany(sql, seq_of_params)
        self.conn.commit()

    def get(self, sql: str, params: Iterable[Any] | None = None) -> Optional[dict]:
        cur = self.conn.cursor()
        cur.execute(sql, params or ())
        return cur.fetchone()

    def close(self) -> None:
        self.conn.close()



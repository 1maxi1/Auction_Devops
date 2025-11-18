import sqlite3
from pathlib import Path
from typing import Any, Iterable, Optional


class AuctionDB:
    def __init__(self, db_path: str = "auction.db") -> None:
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._ensure_schema()

    def _ensure_schema(self) -> None:
        cur = self.conn.cursor()
        cur.executescript(
            """
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS participants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_info TEXT,
                notes TEXT
            );

            CREATE TABLE IF NOT EXISTS auctions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                starts_at TEXT NOT NULL,
                description TEXT
            );

            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                auction_id INTEGER NOT NULL REFERENCES auctions(id) ON DELETE CASCADE,
                seller_id INTEGER NOT NULL REFERENCES participants(id),
                lot_number TEXT NOT NULL,
                title TEXT NOT NULL,
                start_price REAL NOT NULL CHECK (start_price >= 0),
                description TEXT,
                UNIQUE (auction_id, lot_number)
            );

            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER NOT NULL UNIQUE REFERENCES items(id) ON DELETE CASCADE,
                buyer_id INTEGER NOT NULL REFERENCES participants(id),
                sold_price REAL NOT NULL CHECK (sold_price >= 0),
                sold_at TEXT NOT NULL
            );
            """
        )
        self.conn.commit()

    def query(self, sql: str, params: Iterable[Any] | None = None) -> list[sqlite3.Row]:
        cur = self.conn.cursor()
        cur.execute(sql, params or [])
        rows = cur.fetchall()
        return rows

    def execute(self, sql: str, params: Iterable[Any] | None = None) -> int:
        cur = self.conn.cursor()
        cur.execute(sql, params or [])
        self.conn.commit()
        return cur.lastrowid

    def executemany(self, sql: str, seq_of_params: Iterable[Iterable[Any]]) -> None:
        cur = self.conn.cursor()
        cur.executemany(sql, seq_of_params)
        self.conn.commit()

    def get(self, sql: str, params: Iterable[Any] | None = None) -> Optional[sqlite3.Row]:
        cur = self.conn.cursor()
        cur.execute(sql, params or [])
        return cur.fetchone()

    def close(self) -> None:
        self.conn.close()



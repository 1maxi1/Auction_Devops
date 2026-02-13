from __future__ import annotations

import argparse

from db import AuctionDB


def delete_auction(name: str) -> None:
    db = AuctionDB()
    try:
        auction = db.get("SELECT id FROM auctions WHERE name = %s", (name,))
        if not auction:
            print(f"Аукцион '{name}' не найден.")
            return
        db.execute("DELETE FROM auctions WHERE id = %s", (auction["id"],))
        print(f"Аукцион '{name}' удалён.")
    finally:
        db.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Утилита для операций с аукционами.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    delete_parser = subparsers.add_parser("delete-auction", help="Удалить аукцион по названию.")
    delete_parser.add_argument("name", help="Название аукциона")

    args = parser.parse_args()

    if args.command == "delete-auction":
        delete_auction(args.name)


if __name__ == "__main__":
    main()



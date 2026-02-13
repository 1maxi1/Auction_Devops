from __future__ import annotations

from datetime import datetime, timedelta
from typing import Dict

from db import AuctionDB


def wipe_tables(db: AuctionDB) -> None:
    db.execute("DELETE FROM sales")
    db.execute("DELETE FROM items")
    db.execute("DELETE FROM auctions")
    db.execute("DELETE FROM participants")


def add_participants(db: AuctionDB) -> Dict[str, int]:
    participants = [
        ("Антик Групп", "info@antik-group.example", "Постоянный поставщик"),
        ("Галерея Сапфир", "sapphire@example", "Крупная галерея"),
        ("Иван Орлов", "+7 900 123 45 67", "Частный коллекционер"),
        ("Елена Верес", "+7 921 555 11 44", "Специалист по живописи"),
        ("Студия «Артлайн»", "contact@artline.example", None),
        ("Алексей Нестеров", "+7 981 777 22 33", "Покупатель- инвестор"),
    ]
    mapping: Dict[str, int] = {}
    for name, contact, notes in participants:
        participant_id = db.execute(
            """
            INSERT INTO participants (name, contact_info, notes)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (name, contact, notes),
        )
        mapping[name] = participant_id
    return mapping


def add_auctions(db: AuctionDB) -> Dict[str, int]:
    base = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
    auctions = [
        ("Весенний салон", "Москва", base + timedelta(days=3), "Живопись 19-20 вв."),
        ("Летние торги", "Санкт-Петербург", base + timedelta(days=30), "Европейский фарфор"),
        ("Вечер современного искусства", "Москва", base - timedelta(days=15), "Современные авторы"),
        ("Коллекция серебра", "Казань", base + timedelta(days=45), "Столовое серебро XVIII-XIX вв."),
    ]
    mapping: Dict[str, int] = {}
    for name, location, starts_at, desc in auctions:
        auction_id = db.execute(
            """
            INSERT INTO auctions (name, location, starts_at, description)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (name, location, starts_at.isoformat(timespec="minutes"), desc),
        )
        mapping[name] = auction_id
    return mapping


def add_items(db: AuctionDB, participants: Dict[str, int], auctions: Dict[str, int]) -> Dict[str, int]:
    items = [
        ("Весенний салон", "Антик Групп", "101", "Пейзаж «Утро в горах»", 250_000, "Полотно, масло, 1902 г."),
        ("Весенний салон", "Иван Орлов", "102", "Портрет дамы", 180_000, "Холст, масло, 1898 г."),
        ("Летние торги", "Галерея Сапфир", "201", "Чайный сервиз Мейсен", 320_000, "Сервиз из 12 предметов"),
        ("Летние торги", "Студия «Артлайн»", "202", "Ваза Севр", 150_000, "Фарфор, позолота"),
        ("Вечер современного искусства", "Елена Верес", "301", "Инсталляция «Пульс города»", 90_000, "Смешанная техника, 2018"),
        ("Вечер современного искусства", "Антик Групп", "302", "Графика «Контуры»", 60_000, "Бумага, тушь"),
        ("Коллекция серебра", "Студия «Артлайн»", "401", "Серебряный кофейник", 210_000, "Россия, 1875 г."),
        ("Коллекция серебра", "Антик Групп", "402", "Комплект подсвечников", 170_000, "Франция, 1860 г."),
    ]
    mapping: Dict[str, int] = {}
    for auction_name, seller_name, lot, title, price, desc in items:
        auction_id = auctions[auction_name]
        seller_id = participants[seller_name]
        item_id = db.execute(
            """
            INSERT INTO items (auction_id, seller_id, lot_number, title, start_price, description)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (auction_id, seller_id, lot, title, price, desc),
        )
        mapping[title] = item_id
    return mapping


def add_sales(db: AuctionDB, items: Dict[str, int], participants: Dict[str, int]) -> None:
    buyers = {
        "Антик Групп": participants["Антик Групп"],
        "Галерея Сапфир": participants["Галерея Сапфир"],
        "Иван Орлов": participants["Иван Орлов"],
        "Елена Верес": participants["Елена Верес"],
        "Студия «Артлайн»": participants["Студия «Артлайн»"],
        "Алексей Нестеров": participants["Алексей Нестеров"],
    }
    now = datetime.now()
    sales = [
        ("Пейзаж «Утро в горах»", "Алексей Нестеров", 315_000, now - timedelta(days=14)),
        ("Портрет дамы", "Антик Групп", 210_000, now - timedelta(days=13)),
        ("Чайный сервиз Мейсен", "Елена Верес", 380_000, now - timedelta(days=1)),
        ("Инсталляция «Пульс города»", "Галерея Сапфир", 125_000, now - timedelta(days=10)),
        ("Графика «Контуры»", "Иван Орлов", 95_000, now - timedelta(days=9)),
    ]
    for title, buyer_name, price, sold_at in sales:
        db.execute(
            """
            INSERT INTO sales (item_id, buyer_id, sold_price, sold_at)
            VALUES (%s, %s, %s, %s)
            """,
            (
                items[title],
                buyers[buyer_name],
                price,
                sold_at.isoformat(timespec="minutes"),
            ),
        )


def main() -> None:
    db = AuctionDB()
    try:
        wipe_tables(db)
        participants = add_participants(db)
        auctions = add_auctions(db)
        items = add_items(db, participants, auctions)
        add_sales(db, items, participants)
        print("База данных успешно заполнена тестовыми данными.")
    finally:
        db.close()


if __name__ == "__main__":
    main()



from __future__ import annotations

from datetime import date, timedelta
from typing import Iterable

from flask import (
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
)

from db import AuctionDB

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret"


def get_db() -> AuctionDB:
    if "db" not in g:
        g.db = AuctionDB()
    return g.db


@app.teardown_appcontext
def close_db(_: BaseException | None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def default_period(days: int = 30) -> tuple[str, str]:
    period_end = date.today()
    period_start = period_end - timedelta(days=days)
    return period_start.isoformat(), period_end.isoformat()


def period_from_request(days: int = 30) -> tuple[str, str]:
    start_default, end_default = default_period(days)
    start = request.args.get("start") or start_default
    end = request.args.get("end") or end_default
    return start, end


@app.route("/")
def index():
    db = get_db()
    upcoming = db.query(
        """
        SELECT id, name, location, starts_at, description
        FROM auctions
        ORDER BY starts_at
        LIMIT 5
        """
    )
    totals = {
        "auctions": db.get("SELECT COUNT(*) AS c FROM auctions")["c"],
        "participants": db.get("SELECT COUNT(*) AS c FROM participants")["c"],
        "items_count": db.get("SELECT COUNT(*) AS c FROM items")["c"],
        "sales": db.get("SELECT COUNT(*) AS c FROM sales")["c"],
        "revenue": db.get("SELECT COALESCE(SUM(sold_price), 0) AS total FROM sales")[
            "total"
        ],
    }
    top_sellers = db.query(
        """
        SELECT p.name, SUM(s.sold_price) AS total
        FROM participants p
        JOIN items i ON i.seller_id = p.id
        JOIN sales s ON s.item_id = i.id
        GROUP BY p.id
        ORDER BY total DESC
        LIMIT 5
        """
    )
    return render_template(
        "index.html",
        upcoming=upcoming,
        totals=totals,
        top_sellers=top_sellers,
    )


@app.route("/auctions")
def auctions():
    db = get_db()
    start, end = period_from_request()
    location = request.args.get("location", "")

    clauses: list[str] = []
    params: list[str] = []
    if start:
        clauses.append("date(starts_at) >= %s")
        params.append(start)
    if end:
        clauses.append("date(starts_at) <= %s")
        params.append(end)
    if location:
        clauses.append("location = %s")
        params.append(location)

    where_sql = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    auctions = db.query(
        f"""
        SELECT id, name, location, starts_at, description
        FROM auctions
        {where_sql}
        ORDER BY starts_at DESC
        """,
        params,
    )
    locations = db.query(
        "SELECT location FROM auctions GROUP BY location ORDER BY LOWER(location)"
    )
    return render_template(
        "auctions.html",
        auctions=auctions,
        start=start,
        end=end,
        location=location,
        locations=locations,
    )


@app.route("/auctions/add", methods=["GET", "POST"])
def add_auction():
    db = get_db()
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        location = request.form.get("location", "").strip()
        starts_at = request.form.get("starts_at", "").strip()
        description = request.form.get("description", "").strip()
        if not (name and location and starts_at):
            flash("Заполните название, место и дату проведения.", "danger")
            return redirect(url_for("add_auction"))
        db.execute(
            """
            INSERT INTO auctions (name, location, starts_at, description)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (name, location, starts_at, description),
        )
        flash("Аукцион добавлен.", "success")
        return redirect(url_for("auctions"))

    return render_template("add_auction.html")


@app.route("/items/add", methods=["GET", "POST"])
def add_item():
    db = get_db()
    auctions = db.query(
        "SELECT id, name, starts_at FROM auctions ORDER BY starts_at DESC"
    )
    participants = db.query("SELECT id, name FROM participants ORDER BY LOWER(name)")
    if not auctions or not participants:
        flash("Добавьте хотя бы один аукцион и участника.", "warning")
        return render_template(
            "add_item.html", auctions=auctions, participants=participants
        )

    if request.method == "POST":
        auction_id = request.form.get("auction_id")
        seller_id = request.form.get("seller_id")
        lot_number = request.form.get("lot_number", "").strip()
        title = request.form.get("title", "").strip()
        start_price = request.form.get("start_price", "").strip()
        description = request.form.get("description", "").strip()
        if not all([auction_id, seller_id, lot_number, title, start_price]):
            flash("Заполните обязательные поля.", "danger")
            return redirect(url_for("add_item"))
        try:
            price_value = float(start_price)
        except ValueError:
            flash("Стартовая цена должна быть числом.", "danger")
            return redirect(url_for("add_item"))
        db.execute(
            """
            INSERT INTO items (auction_id, seller_id, lot_number, title, start_price, description)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (auction_id, seller_id, lot_number, title, price_value, description),
        )
        flash("Предмет добавлен на аукцион.", "success")
        return redirect(url_for("auctions"))

    return render_template(
        "add_item.html",
        auctions=auctions,
        participants=participants,
    )


def _unsold_items(db: AuctionDB) -> Iterable[dict]:
    return db.query(
        """
        SELECT i.id,
               i.title,
               i.lot_number,
               a.name AS auction_name,
               a.starts_at
        FROM items i
        JOIN auctions a ON a.id = i.auction_id
        LEFT JOIN sales s ON s.item_id = i.id
        WHERE s.id IS NULL
        ORDER BY a.starts_at DESC
        """
    )


@app.route("/sales/add", methods=["GET", "POST"])
def add_sale():
    db = get_db()
    items = _unsold_items(db)
    buyers = db.query("SELECT id, name FROM participants ORDER BY LOWER(name)")
    if not items:
        flash("Нет доступных предметов для продажи.", "warning")
    if not buyers:
        flash("Добавьте хотя бы одного покупателя.", "warning")
    if request.method == "POST":
        item_id = request.form.get("item_id")
        buyer_id = request.form.get("buyer_id")
        sold_price = request.form.get("sold_price", "").strip()
        sold_at = request.form.get("sold_at", "").strip()
        if not all([item_id, buyer_id, sold_price, sold_at]):
            flash("Заполните все поля продажи.", "danger")
            return redirect(url_for("add_sale"))
        try:
            price_value = float(sold_price)
        except ValueError:
            flash("Цена продажи должна быть числом.", "danger")
            return redirect(url_for("add_sale"))
        exists = db.get("SELECT id FROM sales WHERE item_id = %s", (item_id,))
        if exists:
            flash("Предмет уже продан.", "danger")
            return redirect(url_for("add_sale"))
        db.execute(
            """
            INSERT INTO sales (item_id, buyer_id, sold_price, sold_at)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (item_id, buyer_id, price_value, sold_at),
        )
        flash("Продажа сохранена.", "success")
        return redirect(url_for("sold_items"))

    return render_template("add_sale.html", items=items, buyers=buyers)


@app.route("/reports/auction-revenue")
def auction_revenue():
    db = get_db()
    rows = db.query(
        """
        SELECT a.id,
               a.name,
               a.location,
               a.starts_at,
               COALESCE(SUM(s.sold_price), 0) AS revenue
        FROM auctions a
        LEFT JOIN items i ON i.auction_id = a.id
        LEFT JOIN sales s ON s.item_id = i.id
        GROUP BY a.id
        ORDER BY revenue DESC, a.starts_at DESC
        """
    )
    return render_template("auction_revenue.html", auctions=rows)


@app.route("/reports/sold-items")
def sold_items():
    db = get_db()
    start, end = period_from_request()
    rows = db.query(
        """
        SELECT i.title,
               i.lot_number,
               a.name AS auction_name,
               s.sold_price,
               s.sold_at,
               buyers.name AS buyer_name
        FROM sales s
        JOIN items i ON i.id = s.item_id
        JOIN auctions a ON a.id = i.auction_id
        JOIN participants buyers ON buyers.id = s.buyer_id
        WHERE date(s.sold_at) BETWEEN %s AND %s
        ORDER BY s.sold_at DESC
        """,
        (start, end),
    )
    return render_template("sold_items.html", sales=rows, start=start, end=end)


@app.route("/reports/seller-revenue")
def seller_revenue():
    db = get_db()
    start, end = period_from_request()
    rows = db.query(
        """
        SELECT sellers.id,
               sellers.name,
               COALESCE(SUM(s.sold_price), 0) AS total
        FROM participants sellers
        JOIN items i ON i.seller_id = sellers.id
        JOIN sales s ON s.item_id = i.id
        WHERE date(s.sold_at) BETWEEN %s AND %s
        GROUP BY sellers.id
        ORDER BY total DESC
        """,
        (start, end),
    )
    return render_template(
        "seller_revenue.html",
        sellers=rows,
        start=start,
        end=end,
    )


@app.route("/reports/active-buyers")
def buyers_in_period():
    db = get_db()
    start, end = period_from_request()
    rows = db.query(
        """
        SELECT DISTINCT buyers.id, buyers.name
        FROM participants buyers
        JOIN sales s ON s.buyer_id = buyers.id
        WHERE date(s.sold_at) BETWEEN %s AND %s
        ORDER BY buyers.name
        """,
        (start, end),
    )
    return render_template(
        "buyers.html",
        buyers=rows,
        start=start,
        end=end,
        include_counts=False,
    )


@app.route("/reports/buyer-counts")
def buyer_counts():
    db = get_db()
    start, end = period_from_request()
    rows = db.query(
        """
        SELECT buyers.id, buyers.name, COUNT(s.id) AS items_bought
        FROM participants buyers
        JOIN sales s ON s.buyer_id = buyers.id
        WHERE date(s.sold_at) BETWEEN ? AND ?
        GROUP BY buyers.id
        ORDER BY items_bought DESC, buyers.name
        """,
        (start, end),
    )
    return render_template(
        "buyer_counts.html",
        buyers=rows,
        start=start,
        end=end,
    )


@app.route("/reports/sellers-participated")
def sellers_participated():
    db = get_db()
    start, end = period_from_request()
    rows = db.query(
        """
        SELECT DISTINCT sellers.id, sellers.name
        FROM participants sellers
        JOIN items i ON i.seller_id = sellers.id
        JOIN auctions a ON a.id = i.auction_id
        WHERE date(a.starts_at) BETWEEN %s AND %s
        ORDER BY sellers.name
        """,
        (start, end),
    )
    return render_template(
        "seller_participation.html",
        sellers=rows,
        start=start,
        end=end,
    )


@app.route("/participants", methods=["GET", "POST"])
def participants():
    db = get_db()
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        contact = request.form.get("contact_info", "").strip()
        notes = request.form.get("notes", "").strip()
        if not name:
            flash("Имя участника обязательно.", "danger")
            return redirect(url_for("participants"))
        db.execute(
            """
            INSERT INTO participants (name, contact_info, notes)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (name, contact, notes),
        )
        flash("Участник добавлен.", "success")
        return redirect(url_for("participants"))
    rows = db.query("SELECT * FROM participants ORDER BY LOWER(name)")
    return render_template("participants.html", participants=rows)


@app.route("/participants/<int:participant_id>/edit", methods=["GET", "POST"])
def edit_participant(participant_id: int):
    db = get_db()
    participant = db.get(
        "SELECT * FROM participants WHERE id = %s", (participant_id,)
    )
    if participant is None:
        flash("Участник не найден.", "danger")
        return redirect(url_for("participants"))
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        contact = request.form.get("contact_info", "").strip()
        notes = request.form.get("notes", "").strip()
        if not name:
            flash("Имя участника обязательно.", "danger")
            return redirect(url_for("edit_participant", participant_id=participant_id))
        db.execute(
            """
            UPDATE participants
            SET name = %s, contact_info = %s, notes = %s
            WHERE id = %s
            """,
            (name, contact, notes, participant_id),
        )
        flash("Данные участника обновлены.", "success")
        return redirect(url_for("participants"))
    return render_template("edit_participant.html", participant=participant)


if __name__ == "__main__":
    import os
    debug_mode = os.getenv("FLASK_ENV") == "development" or os.getenv("FLASK_DEBUG") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)


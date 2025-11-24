# Auction_Devops
sudo apt-get install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io



test@test-VirtualBox:~$ sudo apt-get install -y ca-certificates curl gnupg lsb-release
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ca-certificates is already the newest version (20240203).
ca-certificates set to manually installed.
gnupg is already the newest version (2.4.4-2ubuntu17.3).
gnupg set to manually installed.
lsb-release is already the newest version (12.0-2).
lsb-release set to manually installed.
The following NEW packages will be installed:
  curl
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 226 kB of archives.
After this operation, 534 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 curl amd64 8.5.0-2ubuntu10.6 [226 kB]
Fetched 226 kB in 0s (614 kB/s)
Selecting previously unselected package curl.
(Reading database ... 153241 files and directories currently installed.)
Preparing to unpack .../curl_8.5.0-2ubuntu10.6_amd64.deb ...
Unpacking curl (8.5.0-2ubuntu10.6) ...
Setting up curl (8.5.0-2ubuntu10.6) ...
Processing triggers for man-db (2.12.0-4build2) ...
test@test-VirtualBox:~$ sudo mkdir -p /etc/apt/keyrings
test@test-VirtualBox:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
test@test-VirtualBox:~$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
test@test-VirtualBox:~$ sudo apt update
Get:1 https://download.docker.com/linux/ubuntu noble InRelease [48.5 kB]
Hit:2 http://archive.ubuntu.com/ubuntu noble InRelease    
Hit:3 https://packages.microsoft.com/repos/code stable InRelease
Get:4 https://download.docker.com/linux/ubuntu noble/stable amd64 Packages [36.9 kB]
Get:5 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]
Get:6 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
Get:7 http://archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
Reading package lists... Done     
E: Release file for http://security.ubuntu.com/ubuntu/dists/noble-security/InRelease is not valid yet (invalid for another 16h 17min 38s). Updates for this repository will not be applied.
E: Release file for http://archive.ubuntu.com/ubuntu/dists/noble-updates/InRelease is not valid yet (invalid for another 16h 19min 23s). Updates for this repository will not be applied.
E: Release file for http://archive.ubuntu.com/ubuntu/dists/noble-backports/InRelease is not valid yet (invalid for another 16h 22min 14s). Updates for this repository will not be applied.
test@test-VirtualBox:~$ sudo apt install docker-ce docker-ce-cli containerd.io
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  docker-buildx-plugin docker-ce-rootless-extras
  docker-compose-plugin git git-man liberror-perl
  libslirp0 pigz slirp4netns
Suggested packages:
  cgroupfs-mount | cgroup-lite docker-model-plugin
  git-daemon-run | git-daemon-sysvinit git-doc git-email
  git-gui gitk gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce
  docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin git git-man liberror-perl
  libslirp0 pigz slirp4netns
0 upgraded, 12 newly installed, 0 to remove and 0 not upgraded.
Need to get 101 MB of archives.
After this operation, 426 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 https://download.docker.com/linux/ubuntu noble/stable amd64 containerd.io amd64 2.1.5-1~ubuntu.24.04~noble [22.4 MB]
Get:2 http://archive.ubuntu.com/ubuntu noble/universe amd64 pigz amd64 2.8-1 [65.6 kB]
Get:3 http://archive.ubuntu.com/ubuntu noble/main amd64 liberror-perl all 0.17029-2 [25.6 kB]
Get:4 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 git-man all 1:2.43.0-1ubuntu7.3 [1,100 kB]
Get:5 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce-cli amd64 5:29.0.2-1~ubuntu.24.04~noble [16.3 MB]
Get:6 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 git amd64 1:2.43.0-1ubuntu7.3 [3,680 kB]
Get:7 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce amd64 5:29.0.2-1~ubuntu.24.04~noble [20.3 MB]
Get:8 http://archive.ubuntu.com/ubuntu noble/main amd64 libslirp0 amd64 4.7.0-1ubuntu3 [63.8 kB]
Get:9 http://archive.ubuntu.com/ubuntu noble/universe amd64 slirp4netns amd64 1.2.1-1build2 [34.9 kB]
Get:10 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-buildx-plugin amd64 0.30.0-1~ubuntu.24.04~noble [16.4 MB]
Get:11 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce-rootless-extras amd64 5:29.0.2-1~ubuntu.24.04~noble [6,383 kB]
Get:12 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-compose-plugin amd64 2.40.3-1~ubuntu.24.04~noble [14.3 MB]
Fetched 101 MB in 4s (27.8 MB/s)                 
Selecting previously unselected package containerd.io.
(Reading database ... 153248 files and directories currentl
y installed.)
Preparing to unpack .../00-containerd.io_2.1.5-1~ubuntu.24.
04~noble_amd64.deb ...
Unpacking containerd.io (2.1.5-1~ubuntu.24.04~noble) ...
Selecting previously unselected package docker-ce-cli.
Preparing to unpack .../01-docker-ce-cli_5%3a29.0.2-1~ubunt
u.24.04~noble_amd64.deb ...
Unpacking docker-ce-cli (5:29.0.2-1~ubuntu.24.04~noble) ...
Selecting previously unselected package docker-ce.
Preparing to unpack .../02-docker-ce_5%3a29.0.2-1~ubuntu.24
.04~noble_amd64.deb ...
Unpacking docker-ce (5:29.0.2-1~ubuntu.24.04~noble) ...
Selecting previously unselected package pigz.
Preparing to unpack .../03-pigz_2.8-1_amd64.deb ...
Unpacking pigz (2.8-1) ...
Selecting previously unselected package docker-buildx-plugi
n.
Preparing to unpack .../04-docker-buildx-plugin_0.30.0-1~ub
untu.24.04~noble_amd64.deb ...
Unpacking docker-buildx-plugin (0.30.0-1~ubuntu.24.04~noble
) ...
Selecting previously unselected package docker-ce-rootless-
extras.
Preparing to unpack .../05-docker-ce-rootless-extras_5%3a29
.0.2-1~ubuntu.24.04~noble_amd64.deb ...
Unpacking docker-ce-rootless-extras (5:29.0.2-1~ubuntu.24.0
4~noble) ...
Selecting previously unselected package docker-compose-plug
in.
Preparing to unpack .../06-docker-compose-plugin_2.40.3-1~u
buntu.24.04~noble_amd64.deb ...
Unpacking docker-compose-plugin (2.40.3-1~ubuntu.24.04~nobl
e) ...
Selecting previously unselected package liberror-perl.
Preparing to unpack .../07-liberror-perl_0.17029-2_all.deb 
...
Unpacking liberror-perl (0.17029-2) ...
Selecting previously unselected package git-man.
Preparing to unpack .../08-git-man_1%3a2.43.0-1ubuntu7.3_al
l.deb ...
Unpacking git-man (1:2.43.0-1ubuntu7.3) ...
Selecting previously unselected package git.
Preparing to unpack .../09-git_1%3a2.43.0-1ubuntu7.3_amd64.
deb ...
Unpacking git (1:2.43.0-1ubuntu7.3) ...
Selecting previously unselected package libslirp0:amd64.
Preparing to unpack .../10-libslirp0_4.7.0-1ubuntu3_amd64.d
eb ...
Unpacking libslirp0:amd64 (4.7.0-1ubuntu3) ...
Selecting previously unselected package slirp4netns.
Preparing to unpack .../11-slirp4netns_1.2.1-1build2_amd64.
deb ...
Unpacking slirp4netns (1.2.1-1build2) ...
Setting up liberror-perl (0.17029-2) ...
Setting up docker-buildx-plugin (0.30.0-1~ubuntu.24.04~nobl
e) ...
Setting up containerd.io (2.1.5-1~ubuntu.24.04~noble) ...
Created symlink /etc/systemd/system/multi-user.target.wants
/containerd.service → /usr/lib/systemd/system/containerd.se
rvice.
Setting up docker-compose-plugin (2.40.3-1~ubuntu.24.04~nob
le) ...
Setting up docker-ce-cli (5:29.0.2-1~ubuntu.24.04~noble) ..
.
Setting up libslirp0:amd64 (4.7.0-1ubuntu3) ...
Setting up pigz (2.8-1) ...
Setting up git-man (1:2.43.0-1ubuntu7.3) ...
Setting up docker-ce-rootless-extras (5:29.0.2-1~ubuntu.24.
04~noble) ...
Setting up slirp4netns (1.2.1-1build2) ...
Setting up docker-ce (5:29.0.2-1~ubuntu.24.04~noble) ...
Created symlink /etc/systemd/system/multi-user.target.wants
/docker.service → /usr/lib/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/do
cker.socket → /usr/lib/systemd/system/docker.socket.
Setting up git (1:2.43.0-1ubuntu7.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for libc-bin (2.39-0ubuntu8.5) ...
test@test-VirtualBox:~$ sudo apt-get install ./docker-desktop-amd64.deb
Reading package lists... Done
E: Unsupported file ./docker-desktop-amd64.deb given on commandline






-- Таблица участников
CREATE TABLE participants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица аукционов
CREATE TABLE auctions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    starts_at TIMESTAMP NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица товаров
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    auction_id INTEGER NOT NULL REFERENCES auctions(id) ON DELETE CASCADE,
    seller_id INTEGER NOT NULL REFERENCES participants(id) ON DELETE CASCADE,
    lot_number VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    start_price DECIMAL(12, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица продаж
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    item_id INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    buyer_id INTEGER NOT NULL REFERENCES participants(id) ON DELETE CASCADE,
    sold_price DECIMAL(12, 2) NOT NULL,
    sold_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- ВСТАВКА ТЕСТОВЫХ ДАННЫХ
-- ============================================

-- Добавление участников
INSERT INTO participants (name, contact_info, notes) VALUES
    ('Антик Групп', 'info@antik-group.example', 'Постоянный поставщик'),
    ('Галерея Сапфир', 'sapphire@example', 'Крупная галерея'),
    ('Иван Орлов', '+7 900 123 45 67', 'Частный коллекционер'),
    ('Елена Верес', '+7 921 555 11 44', 'Специалист по живописи'),
    ('Студия «Артлайн»', 'contact@artline.example', NULL),
    ('Алексей Нестеров', '+7 981 777 22 33', 'Покупатель-инвестор');

-- Добавление аукционов
INSERT INTO auctions (name, location, starts_at, description) VALUES
    ('Весенний салон', 'Москва', NOW() + INTERVAL '3 days', 'Живопись 19-20 вв.'),
    ('Летние торги', 'Санкт-Петербург', NOW() + INTERVAL '30 days', 'Европейский фарфор'),
    ('Вечер современного искусства', 'Москва', NOW() - INTERVAL '15 days', 'Современные авторы'),
    ('Коллекция серебра', 'Казань', NOW() + INTERVAL '45 days', 'Столовое серебро XVIII-XIX вв.');

-- Добавление товаров
INSERT INTO items (auction_id, seller_id, lot_number, title, start_price, description) VALUES
    (1, 1, '101', 'Пейзаж «Утро в горах»', 250000, 'Полотно, масло, 1902 г.'),
    (1, 3, '102', 'Портрет дамы', 180000, 'Холст, масло, 1898 г.'),
    (2, 2, '201', 'Чайный сервиз Мейсен', 320000, 'Сервиз из 12 предметов'),
    (2, 5, '202', 'Ваза Севр', 150000, 'Фарфор, позолата'),
    (3, 4, '301', 'Инсталляция «Пульс города»', 90000, 'Смешанная техника, 2018'),
    (3, 1, '302', 'Графика «Контуры»', 60000, 'Бумага, тушь'),
    (4, 5, '401', 'Серебряный кофейник', 210000, 'Россия, 1875 г.'),
    (4, 1, '402', 'Комплект подсвечников', 170000, 'Франция, 1860 г.');

-- Добавление продаж
INSERT INTO sales (item_id, buyer_id, sold_price, sold_at) VALUES
    (1, 6, 315000, NOW() - INTERVAL '14 days'),
    (2, 1, 210000, NOW() - INTERVAL '13 days'),
    (3, 4, 380000, NOW() - INTERVAL '1 days'),
    (5, 2, 125000, NOW() - INTERVAL '10 days'),
    (6, 3, 95000, NOW() - INTERVAL '9 days');

-- Создание индексов для оптимизации
CREATE INDEX idx_auctions_location ON auctions(location);
CREATE INDEX idx_items_auction_id ON items(auction_id);
CREATE INDEX idx_items_seller_id ON items(seller_id);
CREATE INDEX idx_sales_item_id ON sales(item_id);
CREATE INDEX idx_sales_buyer_id ON sales(buyer_id);

-- Вывод информации о заполнении БД
SELECT 'Таблица participants: ' || COUNT(*) as "Участников" FROM participants;
SELECT 'Таблица auctions: ' || COUNT(*) as "Аукционов" FROM auctions;
SELECT 'Таблица items: ' || COUNT(*) as "Товаров" FROM items;
SELECT 'Таблица sales: ' || COUNT(*) as "Продаж" FROM sales;




sudo docker compose exec db psql -U auction_user -d auction_db -c "
SELECT 'participants' as table_name, COUNT(*) as count FROM participants
UNION ALL
SELECT 'auctions', COUNT(*) FROM auctions
UNION ALL
SELECT 'items', COUNT(*) FROM items
UNION ALL
SELECT 'sales', COUNT(*) FROM sales;
"






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
        ORDER BY datetime(starts_at)
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
        clauses.append("date(starts_at) >= ?")
        params.append(start)
    if end:
        clauses.append("date(starts_at) <= ?")
        params.append(end)
    if location:
        clauses.append("location = ?")
        params.append(location)

    where_sql = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    auctions = db.query(
        f"""
        SELECT id, name, location, starts_at, description
        FROM auctions
        {where_sql}
        ORDER BY datetime(starts_at) DESC
        """,
        params,
    )
    locations = db.query(
        "SELECT DISTINCT location FROM auctions ORDER BY location COLLATE NOCASE"
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
            VALUES (?, ?, ?, ?)
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
        "SELECT id, name, starts_at FROM auctions ORDER BY datetime(starts_at) DESC"
    )
    participants = db.query(
        "SELECT id, name FROM participants ORDER BY name COLLATE NOCASE"
    )
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
            VALUES (?, ?, ?, ?, ?, ?)
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
        ORDER BY datetime(a.starts_at) DESC
        """
    )


@app.route("/sales/add", methods=["GET", "POST"])
def add_sale():
    db = get_db()
    items = _unsold_items(db)
    buyers = db.query("SELECT id, name FROM participants ORDER BY name COLLATE NOCASE")
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
        exists = db.get("SELECT id FROM sales WHERE item_id = ?", (item_id,))
        if exists:
            flash("Предмет уже продан.", "danger")
            return redirect(url_for("add_sale"))
        db.execute(
            """
            INSERT INTO sales (item_id, buyer_id, sold_price, sold_at)
            VALUES (?, ?, ?, ?)
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
        ORDER BY revenue DESC, datetime(a.starts_at) DESC
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
        WHERE date(s.sold_at) BETWEEN ? AND ?
        ORDER BY datetime(s.sold_at) DESC
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
        WHERE date(s.sold_at) BETWEEN ? AND ?
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
        WHERE date(s.sold_at) BETWEEN ? AND ?
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
        WHERE date(a.starts_at) BETWEEN ? AND ?
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
            VALUES (?, ?, ?)
            """,
            (name, contact, notes),
        )
        flash("Участник добавлен.", "success")
        return redirect(url_for("participants"))
    rows = db.query("SELECT * FROM participants ORDER BY name COLLATE NOCASE")
    return render_template("participants.html", participants=rows)


@app.route("/participants/<int:participant_id>/edit", methods=["GET", "POST"])
def edit_participant(participant_id: int):
    db = get_db()
    participant = db.get("SELECT * FROM participants WHERE id = ?", (participant_id,))
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
            SET name = ?, contact_info = ?, notes = ?
            WHERE id = ?
            """,
            (name, contact, notes, participant_id),
        )
        flash("Данные участника обновлены.", "success")
        return redirect(url_for("participants"))
    return render_template("edit_participant.html", participant=participant)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



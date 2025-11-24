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











from flask import Flask, render_template_string
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

# Подключение к БД PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://auction_user:auction_pass@db:5432/auction_db')
engine = create_engine(DATABASE_URL)

# HTML шаблон для главной страницы
MAIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Аукционный дом</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }
        h1 { color: #333; }
        .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin: 20px 0; }
        .stat-box { background: #4CAF50; color: white; padding: 20px; border-radius: 5px; text-align: center; }
        .stat-box h2 { margin: 0; font-size: 32px; }
        .stat-box p { margin: 10px 0 0 0; }
        nav { margin: 20px 0; }
        nav a { margin-right: 15px; padding: 10px 15px; background: #2196F3; color: white; text-decoration: none; border-radius: 4px; }
        nav a:hover { background: #1976D2; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #4CAF50; color: white; }
        tr:hover { background-color: #f5f5f5; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏛️ Аукционный дом - Управление коллекцией искусства</h1>
        
        <nav>
            <a href="/">Главная</a>
            <a href="/auctions">Аукционы</a>
            <a href="/items">Предметы</a>
            <a href="/participants">Участники</a>
            <a href="/sales">Продажи</a>
        </nav>
        
        {{ content }}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Главная страница со статистикой"""
    try:
        with engine.connect() as conn:
            participants = conn.execute(text("SELECT COUNT(*) FROM participants")).scalar()
            auctions = conn.execute(text("SELECT COUNT(*) FROM auctions")).scalar()
            items = conn.execute(text("SELECT COUNT(*) FROM items")).scalar()
            sales = conn.execute(text("SELECT COUNT(*) FROM sales")).scalar()
        
        content = f"""
        <div class="stats">
            <div class="stat-box">
                <h2>{participants}</h2>
                <p>Участников</p>
            </div>
            <div class="stat-box">
                <h2>{auctions}</h2>
                <p>Аукционов</p>
            </div>
            <div class="stat-box">
                <h2>{items}</h2>
                <p>Предметов</p>
            </div>
            <div class="stat-box">
                <h2>{sales}</h2>
                <p>Продаж</p>
            </div>
        </div>
        <h2>Добро пожаловать в Аукционный дом!</h2>
        <p>Система управления коллекцией искусства и проведения аукционов.</p>
        <p>Выберите раздел для просмотра детальной информации.</p>
        """
        return render_template_string(MAIN_TEMPLATE, content=content)
    except Exception as e:
        return f"<h1>Ошибка подключения к БД</h1><p>{str(e)}</p>", 500

@app.route('/auctions')
def get_auctions():
    """Список аукционов"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT id, name, location, description, starts_at 
                FROM auctions 
                ORDER BY starts_at DESC
            """))
            auctions = result.fetchall()
        
        table = "<h2>📅 Аукционы</h2><table><tr><th>Название</th><th>Локация</th><th>Описание</th><th>Дата начала</th></tr>"
        for auction in auctions:
            table += f"<tr><td>{auction[1]}</td><td>{auction[2]}</td><td>{auction[3]}</td><td>{auction[4]}</td></tr>"
        table += "</table>"
        
        return render_template_string(MAIN_TEMPLATE, content=table)
    except Exception as e:
        return f"<h1>Ошибка</h1><p>{str(e)}</p>", 500

@app.route('/items')
def get_items():
    """Список товаров"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT items.id, items.title, items.start_price, items.description,
                       auctions.name as auction_name, participants.name as seller_name
                FROM items
                JOIN auctions ON items.auction_id = auctions.id
                JOIN participants ON items.seller_id = participants.id
                ORDER BY items.id DESC
            """))
            items = result.fetchall()
        
        table = "<h2>🎨 Предметы для продажи</h2><table><tr><th>Название</th><th>Начальная цена</th><th>Описание</th><th>Аукцион</th><th>Продавец</th></tr>"
        for item in items:
            table += f"<tr><td>{item[1]}</td><td>{item[2]:,} ₽</td><td>{item[3]}</td><td>{item[4]}</td><td>{item[5]}</td></tr>"
        table += "</table>"
        
        return render_template_string(MAIN_TEMPLATE, content=table)
    except Exception as e:
        return f"<h1>Ошибка</h1><p>{str(e)}</p>", 500

@app.route('/participants')
def get_participants():
    """Список участников"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT id, name, contact_info, notes 
                FROM participants 
                ORDER BY name
            """))
            participants = result.fetchall()
        
        table = "<h2>👥 Участники</h2><table><tr><th>Имя</th><th>Контакт</th><th>Заметки</th></tr>"
        for p in participants:
            notes = p[3] if p[3] else "—"
            table += f"<tr><td>{p[1]}</td><td>{p[2]}</td><td>{notes}</td></tr>"
        table += "</table>"
        
        return render_template_string(MAIN_TEMPLATE, content=table)
    except Exception as e:
        return f"<h1>Ошибка</h1><p>{str(e)}</p>", 500

@app.route('/sales')
def get_sales():
    """Список продаж"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT sales.id, items.title, sales.sold_price, 
                       participants.name as buyer_name, sales.sold_at
                FROM sales
                JOIN items ON sales.item_id = items.id
                JOIN participants ON sales.buyer_id = participants.id
                ORDER BY sales.sold_at DESC
            """))
            sales = result.fetchall()
        
        table = "<h2>💰 История продаж</h2><table><tr><th>Предмет</th><th>Цена продажи</th><th>Покупатель</th><th>Дата</th></tr>"
        for sale in sales:
            table += f"<tr><td>{sale[1]}</td><td>{sale[2]:,} ₽</td><td>{sale[3]}</td><td>{sale[4]}</td></tr>"
        table += "</table>"
        
        return render_template_string(MAIN_TEMPLATE, content=table)
    except Exception as e:
        return f"<h1>Ошибка</h1><p>{str(e)}</p>", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

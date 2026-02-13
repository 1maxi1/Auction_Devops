# Auction_Devops

Веб‑приложение на Flask для управления аукционами, участниками, лотами и продажами.
В качестве СУБД используется **PostgreSQL**.

## Зависимости

Устанавливаются из `requirements.txt`:

- Flask — веб‑фреймворк
- psycopg2-binary — драйвер PostgreSQL

## Настройка PostgreSQL

1. Создайте базу данных (пример для Windows, утилита `psql`):

   ```powershell
   psql -U postgres -c "CREATE DATABASE auction;"
   ```

2. (Опционально) Создайте отдельного пользователя и выдайте ему права на БД.

3. Задайте переменные окружения для подключения (можно в PowerShell перед запуском):

   ```powershell
   $env:DB_NAME = "auction"
   $env:DB_USER = "postgres"      # или имя вашего пользователя
   $env:DB_PASSWORD = "ВашПароль"
   $env:DB_HOST = "localhost"
   $env:DB_PORT = "5432"
   ```

Если переменные не заданы, используются значения по умолчанию:
`DB_NAME=auction`, `DB_USER=postgres`, `DB_PASSWORD=""`, `DB_HOST=localhost`, `DB_PORT=5432`.

## Установка и запуск

1. Создать и активировать виртуальное окружение (пример для Windows PowerShell):

   ```powershell
   python -m venv ve
   .\ve\Scripts\Activate.ps1
   ```

2. Установить зависимости:

   ```powershell
   pip install -r requirements.txt
   ```

3. Убедиться, что PostgreSQL запущен и переменные окружения (`DB_NAME`, `DB_USER`, и т.д.) заданы.

4. Заполнить базу тестовыми данными (создание таблиц произойдет автоматически при первом подключении):

   ```powershell
   python seed_data.py
   ```

5. Запустить сервер разработки:

   ```powershell
   python main.py
   ```

Приложение будет доступно по адресу `http://127.0.0.1:5000/`.


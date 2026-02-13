#!/bin/bash
set -e

echo "Ожидание готовности PostgreSQL..."
echo "Параметры подключения: DB_HOST=$DB_HOST, DB_PORT=$DB_PORT, DB_NAME=$DB_NAME, DB_USER=$DB_USER"

# Ожидаем пока PostgreSQL будет готов к подключениям
for i in {1..60}; do
  result=$(python3 -c "
import psycopg2
import sys
import os
try:
    conn = psycopg2.connect(
        dbname=os.environ.get('DB_NAME', 'auction'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres'),
        host=os.environ.get('DB_HOST', 'postgres'),
        port=int(os.environ.get('DB_PORT', '5432')),
        connect_timeout=3
    )
    conn.close()
    print('SUCCESS')
    sys.exit(0)
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)
" 2>&1)
  
  if echo "$result" | grep -q "SUCCESS"; then
    echo "PostgreSQL готов!"
    break
  fi
  
  if [ $i -eq 60 ]; then
    echo "Ошибка: PostgreSQL недоступен после 60 попыток"
    echo "Последняя ошибка: $result"
    exit 1
  fi
  
  if [ $((i % 5)) -eq 0 ]; then
    echo "Попытка $i/60 - PostgreSQL недоступен: $result"
  fi
  sleep 1
done

# Заполняем базу данных только если она пустая
echo "Проверка наличия данных в базе данных..."
count=$(python3 -c "
import psycopg2
import os
try:
    conn = psycopg2.connect(
        dbname=os.environ.get('DB_NAME', 'auction'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres'),
        host=os.environ.get('DB_HOST', 'postgres'),
        port=int(os.environ.get('DB_PORT', '5432'))
    )
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM participants')
    result = cur.fetchone()[0]
    conn.close()
    print(result)
except Exception as e:
    print('0')
" 2>&1)

if [ "$count" = "0" ] || [ -z "$count" ]; then
    echo "База данных пустая. Заполнение тестовыми данными..."
    python3 seed_data.py
else
    echo "База данных уже содержит данные ($count участников). Пропускаем заполнение."
fi

# Запускаем Flask приложение
echo "Запуск Flask приложения..."
exec python3 main.py

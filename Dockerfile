
FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


EXPOSE 5000


ENV DB_NAME=auction
ENV DB_USER=postgres
ENV DB_HOST=postgres
ENV DB_PORT=5432
ENV FLASK_APP=main.py
ENV FLASK_ENV=production


ENTRYPOINT ["/entrypoint.sh"]

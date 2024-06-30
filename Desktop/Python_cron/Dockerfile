FROM python:3.9-slim

WORKDIR /app

COPY fetch_data.py /app/fetch_data.py
COPY requirements.txt /app/requirements.txt
COPY crontab /etc/cron.d/crontab

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 0644 /etc/cron.d/crontab

RUN crontab /etc/cron.d/crontab

CMD ["cron", "-f"]

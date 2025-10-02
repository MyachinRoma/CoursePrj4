FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY='django-insecure-nb-q@q)aduh@rmwo)pky0ixc%kbhs+r9d!0fgfzz9io$!3&@ef'
ENV CELERY_BROKER_URL='redis://localhost:6379'
ENV CELERY_BACKEND='redis://localhost:6379'

RUN mkdir -p /app/staticfiles
EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000 --timeout 120"]

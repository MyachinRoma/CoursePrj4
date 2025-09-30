# Habits API (clean)

Готовый к GitHub проект Django + DRF.

## Быстрый старт (Poetry)
```bash
# 1) Установить Poetry, если нет
pip install poetry

# 2) Установить зависимости
poetry install

# 3) Переменные окружения
cp .env.sample .env

# 4) Миграции и запуск
poetry run python manage.py migrate
poetry run python manage.py runserver
```

## Тесты
```bash
poetry run pytest
```

## Docker (локально)
```bash
docker compose up --build
```

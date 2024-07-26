FROM python:3.11-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /server
COPY app /server/app
COPY manage.py poetry.lock pyproject.toml  /server/

RUN apt-get update && apt-get install libpq-dev build-essential -y \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install

EXPOSE 6600

CMD gunicorn app.wsgi:application --bind 0.0.0.0:6600

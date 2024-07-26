ARGS = $(filter-out $@,$(MAKECMDGOALS))
COMPOSE_COMMAND=$(shell command -v docker-compose >/dev/null 2>&1 && echo "docker-compose" || echo "docker compose")

build:
	$(COMPOSE_COMMAND) build

clean:
	$(COMPOSE_COMMAND) kill && $(COMPOSE_COMMAND) down --rmi all
	sudo rm -rf data/
	sudo rm -rf statics/
	sudo rm -rf .pytest_cache/

createsuperuser:
	poetry run python manage.py shell -c "from django.contrib.auth.models import User; \
	u, _ = User.objects.get_or_create(email='dev@peopleregister.co'); \
	u.username = 'dev'; \
	u.set_password('people@#register'); \
	u.is_superuser = u.is_staff = True; \
	u.save(); \
	print('Superuser: dev / people@#register');"

statics:
	poetry run python manage.py collectstatic --noinput

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

dbupdate: migrations migrate

dbunaccent:
	$(COMPOSE_COMMAND) exec db psql -U peopleregister -c "CREATE EXTENSION IF NOT EXISTS UNACCENT;"

# atualizar para peoples
fixtures:
	$(COMPOSE_COMMAND) run --rm app python manage.py loaddata finances/tests/fixtures/users/user.json
	$(COMPOSE_COMMAND) run --rm app python manage.py loaddata finances/tests/fixtures/transactions/transaction.json

# atualizar para peoples
dump:
	$(COMPOSE_COMMAND) run --rm app python manage.py dumpdata accounts.user --indent=2 --format=json > finances/tests/fixtures/users/user.json
	$(COMPOSE_COMMAND) run --rm app python manage.py dumpdata wallets.transaction --indent=2 --format=json > finances/tests/fixtures/transactions/transaction.json

precommit:
	pre-commit install
	pre-commit autoupdate

lint:
	poetry run ruff check . && poetry run ruff check . --diff

format:
	poetry run ruff check . --fix && poetry run ruff format .

services:
	$(COMPOSE_COMMAND) up -d db

setup: build services dbupdate dbunaccent createsuperuser statics

bash:
	$(COMPOSE_COMMAND) run --rm $(ARGS) sh

test:
	poetry run pytest -s

shell_plus:
	poetry run python manage.py shell_plus

stop:
	$(COMPOSE_COMMAND) down --remove-orphans

run:
	poetry run python manage.py runserver 0.0.0.0:6600

default: run

run:
	docker-compose up -d

build: purge docker-build

docker-build:
	docker-compose build

stop:
	docker-compose down

logs:
	docker-compose logs -tf

cli:
	docker-compose run --rm cli sh

migrate:
	docker-compose run --rm cli python manage.py migrate ${app_name}

makemigrations:
	docker-compose run --rm cli python manage.py makemigrations ${app_name}

reset-db:
	docker-compose run --rm cli python manage.py reset_db -c --noinput

createsuperuser:
	docker-compose run --rm cli python manage.py createsuperuser

purge:
	docker-compose down -v --remove-orphans
	rm -rf ./api/static/*

app:
	docker-compose run --rm cli python manage.py startapp ${app_name}

test:
	docker-compose run --rm cli python manage.py test
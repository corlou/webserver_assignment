SHELL := /bin/bash

.default: start

install:
	python -m pip install -r requirements.txt

start:
	python app.py

test:
	python -m pytest -W ignore::DeprecationWarning

db-start:
	docker pull postgres
	docker run --name polecalendar2 \
		--env POSTGRES_USER=admin \
		--env POSTGRES_PASSWORD=password \
		--env POSTGRES_DB=polecalendar2 \
		--publish 5433:5432 \
		--detach \
		postgres

db-stop:
	docker rm -f polecalendar2

deps:
	python -m pip freeze > requirements.txt
build:
	docker-compose build

up:
	docker-compose up

upd:
	docker-compose up -d

stop:
	docker-compose stop

logs:
	docker-compose logs -f

clean:
	docker-compose rm --force
	rm -rf ./db/*

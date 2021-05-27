SHELL := bash

build:
	docker-compose up -d --build

develop:
	docker run -it --rm -v=$(PWD)/RestaurantReservation/backend:/api --network=restaurantreservation_restaurant_net restaurantreservation_api:latest bash

api:
	docker run -it --rm restaurantreservation_api:latest bash

postgres:
	docker exec -it restaurantreservation_postgres-db_1 psql -U postgres

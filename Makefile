SHELL := bash

build:
	docker-compose up -d --build

develop:
	docker run -it --rm -v=$(PWD)/RestaurantReservation/backend:/api --network=restaurantreservation_restaurant_net -p 5000:5000 restaurantreservation_api:latest bash

api:
	docker exec -it restaurantreservation_api_1 bash

postgres:
	docker exec -it restaurantreservation_postgres-db_1 psql -U postgres

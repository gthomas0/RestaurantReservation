SHELL := bash

build:
	docker-compose up -d --build

develop:
	docker run -it --rm -v=$(pwd)/RestaurantReservation/backend:/api --network=restaurantreservation_restaurant_net restaurantreservation_api:latest bash

api:
	docker run -it --rm restaurantreservation_api:latest bash
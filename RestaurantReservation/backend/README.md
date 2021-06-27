# Restaurant Reservation Backend
The backend of this application is built in Flask with a Postgres database. Both are encapsulated in docker containers
on the same docker network to enable communication on a private network. 

Look at the main [`README`](./README.md) for more information on how to run the application in full.

## API Endpoints

`POST '/schedule'`
- Post a csv file containing the restaurant schedules to populate the postgresql database
- Request Arguments: csv file
- Example cURL: `curl -F "schedule=@$(pwd)/RestaurantReservation/backend/csv_data/schedule.csv" http://localhost:5000/schedule`
- Example Response:
```json
{
  "success": true
}
```

`GET '/schedule'`
- Get a list of restaurant names which are open on a given day and time
- Request Arguments: Python Datetime String
- Example cURL: `curl -G --data-urlencode "datetimestr=2021-05-27 12:23:53.350219" http://localhost:5000/schedule`
- Example Response:
```json
{
  "restaurants": [
    "The Cowfish Sushi Burger Bar",  
    "Mandolin", 
    "Neomonde", 
    "Page Road Grill", 
    "Mez Mexican", 
    "Saltbox", 
    "El Rodeo"
  ], 
  "success": true
}
```

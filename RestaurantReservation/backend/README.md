# Restaurant Reservation Application

### Dependencies
In order for this application to run, some dependencies need to be installed.  
  * **Docker** This is the best way to run the application


### Running the Application
To start the application, from the root directory run the following:

```bash
make build
```

After the docker services are running, post the csv file to the database:

```bash
curl -G --data-urlencode "datetimestr=2021-05-27 12:23:53.350219" http://localhost:5000/schedule
```

Now you can query the `/schedule` endpoint for open restaurants!

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

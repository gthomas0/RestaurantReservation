# Restaurant Reservation Backend
The backend of this application is built in Flask with a Postgres database. Both are encapsulated in docker containers
on the same docker network to enable communication on a private network. 

Look at the main [`README`](../../README.md) for more information on how to run the application in full.

## API Auths
These are the API Auth tokens that correspond to each of the User Roles available in Auth0. Due to there not being a frontend with a login page, these were created using the `Machine to Machine Applications` section of Auth0 with the correct permissions.  
Query For Token: 
```
curl --request POST \
--url https://fsnd-gt.us.auth0.com/oauth/token \
--header 'content-type: application/json' \
--data '{"client_id":["REDACTED"],"client_secret":["REDACTED"],"audience":"scheduler","grant_type":"client_credentials"}'
```  
Patron Token: `PLACE TOKEN HERE FOR TESTING`  
Admin Token: `PLACE TOKEN HERE FOR TESTING`


## Domains
You can access this application via Heroku or by running `make build` and accessing the API locally.

Local Domain: `http://localhost:5000`
Heroku Domain: `https://restaurant-reservation-gthomas.herokuapp.com`

## API Endpoints

`POST '/schedules'`
- Post a csv file containing the restaurant schedules to populate the postgresql database
- Request Arguments: csv file
- Example cURL: `curl -F "schedules=@$(pwd)/RestaurantReservation/backend/csv_data/schedule.csv" [DOMAIN]/schedules -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
  "success": true
}
```

`GET '/schedules'`
- Get a list of restaurant names which are open on a given day and time
- Request Arguments: Python Datetime String
- Example cURL: `curl -G --data-urlencode "datetimestr=2021-05-27 12:23:53.350219" [DOMAIN]/schedules -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
  "restaurants": [
    {"id": 1, "name": "The Cowfish Sushi Burger Bar"},  
    {"id": 2, "name": "Mandolin"}, 
    {"id": 3, "name": "Neomonde"}, 
    {"id": 4, "name": "Page Road Grill"}, 
    {"id": 5, "name": "Mez Mexican"}, 
    {"id": 6, "name": "Saltbox"}, 
    {"id": 7, "name": "El Rodeo"}
  ], 
  "success": true
}
```

`DELETE '/schedules'`
- Delete either a specific schedule by ID or all the schedules
- Request Arguments: Integer id (Optional)
- Example cURL: `curl -X DELETE [DOMAIN]/schedules -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "delete": 1
}
```

`GET '/patrons'`
- Get either a specific patron or all the patrons
- Request Arguments: Integer id (Optional)
- Example cURL: `curl [DOMAIN]/patrons -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "patrons": [
        {
            "id": 1,
            "name": "Greg",
            "number": "555-555-5555",
            "email": "fake_email@gmail.com"
        },
        {
            "id": 2,
            "name": "Joe",
            "number": "777-555-5555",
            "email": "gemail@gmail.com"
        }
    ]
}
```

`POST '/patrons'`
- Post a new patron
- Request Arguments: JSON Dict containing patron data (name, number, email)
- Example cURL: `curl -X POST -d '{"name":"Greg","number":"555-555-5555","email":"fake@gmail.com"}' [DOMAIN]/patrons -H "Content-Type: application/json" -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "created": 10
}
```

`PATCH '/patrons'`
- Patch an existing patron
- Request Arguments: Dict containing ID and fields to patch
- Example cURL: `curl -X PATCH -d '{"id":65,"name":"Joe"}' [DOMAIN]/patrons -H "Content-Type: application/json" -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "patron": {
        "id": 65,
        "name": "Joe",
        "number": "555-555-5555",
        "email": "fake_email@gmail.com"
    }
}
```

`DELETE '/patrons'`
- Delete either a specific patron or all the patrons
- Request Arguments: Integer id (Optional)
- Example cURL: `curl -X DELETE [DOMAIN]/patrons -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "delete": 1
}
```

`GET '/reservations'`
- Get all the reservations
- Request Arguments: None
- Example cURL: `curl [DOMAIN]/reservations -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "reservations": [
        {
            "restaurant_id": 2,
            "restaurant_name": "Mandolin",
            "patron_id": 1,
            "patron_name": "Greg",
            "start_time": "Thu, 27 May 2021 12:23:53 GMT"
        }
    ]
}
```

`POST '/reservations'`
- Post a new reservation between a patron and a restaurant
- Request Arguments: Dict containing restaurant_id, patron_id, and start_time
- Example cURL: `curl -X POST -d '{"restaurant_id":"4912","patron_id":"65","start_time":"2021-05-27 12:23:53.350219"}' [DOMAIN]/reservations -H "Content-Type: application/json" -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "created": {
        "restaurant_id": 10,
        "patron_id": 15,
        "start_time": "Thu, 27 May 2021 12:23:53 GMT"
    },
    "success": true
}
```

`DELETE '/reservations'`
- Delete all the reservations
- Request Arguments: None
- Example cURL: `curl -X DELETE [DOMAIN]/reservations -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "delete": 1
}
```

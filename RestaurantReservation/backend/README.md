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
--data '{"client_id":"Q7UxP2fzeOjdkYu69RLGXwFG4QgeGJAH","client_secret":"7rPVVSrO8vl2RjOVIernYquz-oZukUCptt7MaOPOWzelCGsCMN3dwV7SgvIBUS_J","audience":"scheduler","grant_type":"client_credentials"}'
```  
Patron Token: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2Mjk2MzM2MDUsImV4cCI6MTYyOTcyMDAwNSwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6ImdldDpzY2hlZHVsZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6c2NoZWR1bGVzIl19.mDDpyNbCFQkn5KrA9oe0-HzF7vIUtTSoAHx3QBuIL0bHxVt_Uh5QV7gg2wzLDqFHh0xnB3QRvVvezb1uAEINblUcPuUvRHO7247Ouu9B7VE0-PGaYKciBEBcGC4FutHs8lwhaeisSsarXTyHTv5vYYxAwKDJonzUcVVOLQRw4gt892mme1Xlk0NwqPRTv9WoviM2rVtvizpz0inxof9gNYkXaXKvGCg6p4RaqcUwQLaguqdMm-T6IMFu6bEBcr2pO4BX6Z4m4GrKlP66x5Tcp76fhRLssstEXiNLK2AWtNFCaw0VW8mArcy42bhY__5AyD8dR3_qD5NxZQkRjGvjfA`  
Admin Token: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2Mjk2MzM2MjksImV4cCI6MTYyOTcyMDAyOSwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6InBvc3Q6c2NoZWR1bGVzIGdldDpzY2hlZHVsZXMgZGVsZXRlOnNjaGVkdWxlcyBwb3N0OnBhdHJvbnMgcGF0Y2g6cGF0cm9ucyBnZXQ6cmVzZXJ2YXRpb25zIHBvc3Q6cmVzZXJ2YXRpb25zIGdldDpwYXRyb25zIGRlbGV0ZTpwYXRyb25zIGRlbGV0ZTpyZXNlcnZhdGlvbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJwb3N0OnNjaGVkdWxlcyIsImdldDpzY2hlZHVsZXMiLCJkZWxldGU6c2NoZWR1bGVzIiwicG9zdDpwYXRyb25zIiwicGF0Y2g6cGF0cm9ucyIsImdldDpyZXNlcnZhdGlvbnMiLCJwb3N0OnJlc2VydmF0aW9ucyIsImdldDpwYXRyb25zIiwiZGVsZXRlOnBhdHJvbnMiLCJkZWxldGU6cmVzZXJ2YXRpb25zIl19.UiiTemqfPwjaLpYMsEL7lAaamfU1sXrPaGhkPUz7FU3zWHqKvML7aQ5jyv8t58F9oWWkm3xrpxnJG-DCRMKfD4B9EutVHu1Kwjrq0eEIENLS8Xit3RVtt1x3WsYAU8JHy2jQsdRxQo8epDjKdFbFMoKWbLhJn8Tv583BiOnN6tc6BOHm7KH5mN9YRLPdIjLe9QmXzocPhGO3fa6Ye0DJyHWqECPTo9ynwMYNA_fgpa8rONM4Ey4Pfr8Eh5iMEUZl2oPje-TwvhXTghd3xM65sbjYTdflmsQl2ezpYV7UVHZdy-bEKh-Jjr1S7MU4S8_BqwmrXgmsRbhCHQyCJ98cKw`


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

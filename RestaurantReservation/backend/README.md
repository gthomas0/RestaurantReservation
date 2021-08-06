# Restaurant Reservation Backend
The backend of this application is built in Flask with a Postgres database. Both are encapsulated in docker containers
on the same docker network to enable communication on a private network. 

Look at the main [`README`](./README.md) for more information on how to run the application in full.

## API Auths
Patron: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgyMTI3MTAsImV4cCI6MTYyODI5OTExMCwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6ImdldDpzY2hlZHVsZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6c2NoZWR1bGVzIl19.o-RC7u2hmIPA2kB4nHRHCHzYXp_M_O8rhSi-ggTGIwu8MJJcjubslK7bvxN9rFTbRRM7gSqNSYPdtlq6mKDfKo-_5bmEM4xF22UYmLJDLZJOEqvskB4r3G087XsI534XUcmmbHKpnOcJCDwGVSmsuUiSjg623OTvybhEfoVjaTWSizMejumeHQeQtCH5DQZZn6hbEjBY4X_1U5C3Jh3Nag7Oy4lUJy1jIUlN8Pbn47vPmlT2TWTq6IdTI4RaBuBAQU6o0vIThIafUuehdT8nQnjOrKHYHsTt48S-4MUrYDxKyE31ot0ElQszn87EcYiAUhNc7QIRMZxiQuJSDNAbnQ`  
Admin: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgyMTI2ODYsImV4cCI6MTYyODI5OTA4NiwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6InBvc3Q6c2NoZWR1bGVzIGdldDpzY2hlZHVsZXMgZGVsZXRlOnNjaGVkdWxlcyBwb3N0OnBhdHJvbnMgcGF0Y2g6cGF0cm9ucyBnZXQ6cmVzZXJ2YXRpb25zIHBvc3Q6cmVzZXJ2YXRpb25zIGdldDpwYXRyb25zIGRlbGV0ZTpwYXRyb25zIGRlbGV0ZTpyZXNlcnZhdGlvbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJwb3N0OnNjaGVkdWxlcyIsImdldDpzY2hlZHVsZXMiLCJkZWxldGU6c2NoZWR1bGVzIiwicG9zdDpwYXRyb25zIiwicGF0Y2g6cGF0cm9ucyIsImdldDpyZXNlcnZhdGlvbnMiLCJwb3N0OnJlc2VydmF0aW9ucyIsImdldDpwYXRyb25zIiwiZGVsZXRlOnBhdHJvbnMiLCJkZWxldGU6cmVzZXJ2YXRpb25zIl19.UN3j3bkdruWj-jxAxIdIhGOT-ZJbbQZoq8zv8KNKBZwZWVfb1rZKj4Iq6ME0BtFTEEtsAqO8xWDOjwWshO3G0wcK7HhCvT3bmjkcCOWPa0Ssd4KLahAAWap7ZbqTX9_vh3o6Q2GZzZMM7B3wM9EiNRejCcHbAqeMuZyT7AlRaK3BDTzJ0-4ZqeOYgfZWY5BsLlCB7DWBmImW-dk9PXYJ8Xpr72Gwg5xZ9-GS-X1cZCNdtHl__LXBhUSVb-P_PXFqbNdDpbhnVIt-VG5mzpkhtvktJVwDE3Wmjib5MnW2ln8LeQSHyKdLA3A9On0WSwN_34Yg9tkragZE3neJ1WiqxQ`


## API Endpoints

`POST '/schedules'`
- Post a csv file containing the restaurant schedules to populate the postgresql database
- Request Arguments: csv file
- Example cURL: `curl -F "schedules=@$(pwd)/RestaurantReservation/backend/csv_data/schedule.csv" http://localhost:5000/schedules -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
  "success": true
}
```

`GET '/schedules'`
- Get a list of restaurant names which are open on a given day and time
- Request Arguments: Python Datetime String
- Example cURL: `curl -G --data-urlencode "datetimestr=2021-05-27 12:23:53.350219" http://localhost:5000/schedules -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl -X DELETE http://localhost:5000/schedules -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl http://localhost:5000/patrons -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl -X POST -d '{"name":"Greg","number":"555-555-5555","email":"fake@gmail.com"}' http://localhost:5000/patrons -H "Content-Type: application/json" -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl -X PATCH -d '{"id":65,"name":"Joe"}' http://localhost:5000/patrons -H "Content-Type: application/json" -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl -X DELETE http://localhost:5000/patrons -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl http://localhost:5000/reservations -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl -X POST -d '{"restaurant_id":"4912","patron_id":"65","start_time":"2021-05-27 12:23:53.350219"}' http://localhost:5000/reservations -H "Content-Type: application/json" -H "Authorization: Bearer [YOUR_TOKEN]"`
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
- Example cURL: `curl -X DELETE http://localhost:5000/reservations -H "Authorization: Bearer [YOUR_TOKEN]"`
- Example Response:
```json
{
    "success": true,
    "delete": 1
}
```

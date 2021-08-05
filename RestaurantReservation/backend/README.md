# Restaurant Reservation Backend
The backend of this application is built in Flask with a Postgres database. Both are encapsulated in docker containers
on the same docker network to enable communication on a private network. 

Look at the main [`README`](./README.md) for more information on how to run the application in full.

## API Auths
Patron: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgxMjY0MTcsImV4cCI6MTYyODIxMjgxNywiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6ImdldDpzY2hlZHVsZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6c2NoZWR1bGVzIl19.UN_Mmaf8iedaZbrj3OA5teFze2RVM83jQlyATUMDx1w86GIgxCO3EedrK6YrI-CzH4I5a4dk9wIro0zLCJObAUxYTBW9X_tcV-qB7uQ4olrxov_EbQw7EFaRBpRqvkCjSuDKNkx8NqpoxqQGW3wMfV3hbMmByzsVdUz-dkNVN6ZUbT97BQhGo_90x25G8lk5c5PxBEexhB9aGOGCNn8osVHKT2Vq75QUftg40F9hTNs35MMYVOtreO71C-ec344W6GzneLWkgBygCzj4mbhG7npF_c8NHkC5927qqyX-P0rhfscI3ZKMzDlyZUQ_ADc7NTcJocJkDQ3jusLNSEchBw`  
Admin: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgxMzQ3NjQsImV4cCI6MTYyODIyMTE2NCwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6InBvc3Q6c2NoZWR1bGVzIGdldDpzY2hlZHVsZXMgZGVsZXRlOnNjaGVkdWxlcyBwb3N0OnBhdHJvbnMgcGF0Y2g6cGF0cm9ucyBnZXQ6cmVzZXJ2YXRpb25zIHBvc3Q6cmVzZXJ2YXRpb25zIGdldDpwYXRyb25zIGRlbGV0ZTpwYXRyb25zIGRlbGV0ZTpyZXNlcnZhdGlvbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJwb3N0OnNjaGVkdWxlcyIsImdldDpzY2hlZHVsZXMiLCJkZWxldGU6c2NoZWR1bGVzIiwicG9zdDpwYXRyb25zIiwicGF0Y2g6cGF0cm9ucyIsImdldDpyZXNlcnZhdGlvbnMiLCJwb3N0OnJlc2VydmF0aW9ucyIsImdldDpwYXRyb25zIiwiZGVsZXRlOnBhdHJvbnMiLCJkZWxldGU6cmVzZXJ2YXRpb25zIl19.Vs0J_z7fAg8zVZpal1yax6Vep7CFM3uuwQpWYRIaUDXmvkkcHJWJqwMbEsE6XfJuKa9j7T4lSY8KwquaiYiJjV-Hao-ax82Nhh_-nsVml4BZs8aPXJVdEKobZO7_y0or5hmaRUrKvuLkJpMptD0-JYobOMaNfE9o6esFeuIiYDJkCWdaOUtJ25k3-bCsvdJbYuSKWqWb1f55K873VEYnhCqhGLlH6q8mLIX41EmXdSU1jl1ZUHaCcMo-lY6FF96oMrariYW7GRbdT3ogT3fUqt0AOxeEVpDn28PMRHtUcV5z3IODzHRNgKDSsge1hS68g7YZiWflQmj6zWmMZz0B_Q`


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
- Request Arguments: Integer id
- Example cURL: `curl -X DELETE http://localhost:5000/schedules`
- Example Response:
```json

```

`GET '/patrons'`
- Get either a specific patron or all the patrons
- Request Arguments: 
- Example cURL: 
- Example Response:
```json

```

`POST '/patrons'`
- Post a new patron
- Request Arguments: 
- Example cURL: 
- Example Response:
```json

```

`PATCH '/patrons'`
- Patch an existing patron
- Request Arguments: 
- Example cURL: 
- Example Response:
```json

```

`DELETE '/patrons'`
- Delete either a specific patron or all the patrons
- Request Arguments: 
- Example cURL: 
- Example Response:
```json

```

`GET '/reservations'`
- Get all the reservations
- Request Arguments: None
- Example cURL: 
- Example Response:
```json

```

`POST '/reservations'`
- Post a new reservation between a patron and a restaurant
- Request Arguments: 
- Example cURL: 
- Example Response:
```json

```

`DELETE '/reservations'`
- Delete all the reservations
- Request Arguments: None
- Example cURL: 
- Example Response:
```json

```

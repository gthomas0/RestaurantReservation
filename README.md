# Restaurant Reservation Application
This Restaurant Reservation project is meant to be an API that would support a service that would allow restaurants to post schedules for customers to be able to set up reservations. This app would allow customers to make a reservation to different restaurants, or even just query for what the schedules are for the restaurants. All the restaurants in the sample data are local to where I am personally.
### Dependencies
In order for this application to run, some dependencies need to be installed.  
  * **Docker** This is the best way to run the application


### Running the Application
To start the application, from the root directory run the following:

```bash
make build
```

### Backend README
Check out the [`Backend README`](./RestaurantReservation/backend/README.md) for more information on the API endpoints!  
The Backend README goes over API authentications and API endpoints.

### Makefile Commands
`make build`
 - Runs docker-compose for the project. This sets everything up for you!

`make develop`
 - This sets up just the API. If you ran `make build`, you do not need to run this.

`make api`
 - This executes bash in an interactive terminal within the API container built by the `make build` command.

`make postgres`
 - This executes psql in an interactive terminal within the PostgresQL container built by the `make build` command.

`make test`
 - This initializes the python venv and runs pytest within the API container built by the `make build` command.

# Restaurant Reservation Backend

## Connection Details
### Auth0 Account
```
AUTH0_DOMAIN = 'fsnd-gt.us.auth0.com'
API_AUDIENCE = 'scheduler'
```

### Dependencies
In order for this application to run, some dependencies need to be installed.  
**Manual:**
  * **venv** as a tool to create isolated Python environments
  * **postgres** as our database [install here](https://www.postgresql.org/download/)

**Handled by requirements.txt:**
  * **SQLAlchemy ORM** as our ORM Library
  * **

### Running the Backend
From within the `./backend` directory first ensure you are working using your created virtual environment, then pip install the requirements.

**Note:** You will need to install python3.7-dev for python headers for psycopg2 # WSL2/Linux

Python Version: Python 3.7.5

```bash
sudo apt-get install python3.7-dev
pip install -r requirements.txt
```

From within the `./backend/src`, run:
```bash
export FLASK_APP=api.py;
flask run --reload
```

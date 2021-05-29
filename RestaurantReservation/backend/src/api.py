import pandas as pd
import json
from datetime import datetime, time
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sqlalchemy import exc

from .database.models import setup_db, db_drop_and_create_all, Restaurant
from .auth.auth import AuthError, requires_auth
from .utils.date_handler import get_datetime_range, get_day_column, get_day_range, get_time_range, get_weekday


app = Flask(__name__)
setup_db(app)
CORS(app)

# Uncomment this to start fresh with the database
# db_drop_and_create_all()


@app.route('/schedule', methods=['GET', 'POST'])
#@requires_auth('post:schedule')
def post_schedule():
    try:
        if request.method == 'POST':
            if request.files:
                schedule_file = request.files['schedule']
                schedules = dict(pd.read_csv(schedule_file).to_numpy())

                # Handle schedule upload
                for restaurant, schedule in schedules.items():
                    schedule_dict = dict()
                    for single_time in schedule.split('/'):
                        day_range, day_match = get_day_range(single_time)
                        time_range = get_time_range(single_time.split(day_match)[1].strip())
                        time_dict = {d: time_range for d in day_range}
                        schedule_dict.update(time_dict)

                    new_schedule = Restaurant(
                        name=restaurant,
                        sunday=schedule_dict.get('Sun', '00:00-00:00'),
                        monday=schedule_dict.get('Mon', '00:00-00:00'),
                        tuesday=schedule_dict.get('Tues', '00:00-00:00'),
                        wednesday=schedule_dict.get('Wed', '00:00-00:00'),
                        thursday=schedule_dict.get('Thu', '00:00-00:00'),
                        friday=schedule_dict.get('Fri', '00:00-00:00'),
                        saturday=schedule_dict.get('Sat', '00:00-00:00'),
                        hours=str(schedule)
                    )

                    new_schedule.insert()

            return jsonify({
                'success': True
            })

        if request.method == 'GET':
            datetimestr = request.args.get('datetimestr')

            datetime_obj = datetime.strptime(datetimestr, '%Y-%m-%d %H:%M:%S.%f')

            day = get_weekday(datetime_obj.weekday())
            reservation_time = get_datetime_range(f'{datetime_obj.hour}:{datetime_obj.minute}')

            restaurants = Restaurant.query.all()
            open_restaurants = []

            for restaurant in restaurants:
                day_column = get_day_column(restaurant, day)

                start, end = day_column.split('-')
                start_time = get_datetime_range(start)
                end_time = get_datetime_range(end)
                in_time = start_time < reservation_time < end_time

                if in_time:
                    open_restaurants.append(restaurant.name)

            return jsonify({
                'success': True,
                'restaurants': open_restaurants
            })

    except:
        abort(422)


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
    }), 422

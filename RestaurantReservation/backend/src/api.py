import pandas as pd
import json
from datetime import datetime, time
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sqlalchemy import exc

from .database.models import setup_db, Restaurant, Patron
from .auth.auth import AuthError, requires_auth
from .utils.date_handler import get_datetime_range, get_day_column, get_day_range, get_time_range, get_weekday


app = Flask(__name__)
setup_db(app)
CORS(app)


"""
Schedule Section
"""
@app.route('/schedules', methods=['GET'])
@requires_auth('get:schedule')
def get_schedule(jwt):
    try:
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
        abort(404)


@app.route('/schedules', methods=['POST'])
@requires_auth('post:schedule')
def post_schedule(jwt):
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

    except:
        abort(422)


"""
Patron Section
"""
@app.route('/patrons', methods=['POST'])
@requires_auth('POST:patron')
def post_patron(jwt):
    try:
        if request.method == 'POST':
            body = request.get_json()

            new_name = body['name']
            new_number = body['number']
            new_email = body['email']

            patron = Patron(name=new_name,
                            number=new_number,
                            email=new_email)
            patron.insert()

            return jsonify({
                'success': True,
                'created': patron.id
            })
    except:
        abort(422)


@app.route('/patrons/<id>', methods=['PATCH'])
@requires_auth('PATCH:patron')
def patch_reservation(jwt, id):
    if request.method == 'PATCH':
        patron = Patron.query.get(id)

        if patron:
            try:
                body = request.get_json()

                new_name = body.get('name')
                new_number = body.get('number')
                new_email = body.get('email')

                if new_name:
                    patron.name = new_name
                if new_number:
                    patron.number = new_number
                if new_email:
                    patron.email = new_email

                patron.update()

                return jsonify({
                    'success': True,
                    'patron': patron.format()
                })
            except:
                abort(422)
        else:
            abort(404)


"""
Reservation Section
"""
@app.route('/reservations', methods=['GET'])
@requires_auth('get:reservation')
def get_reservation(jwt):
    pass


@app.route('/reservations', methods=['POST'])
@requires_auth('POST:reservation')
def post_reservation(jwt):
    pass


@app.route('/reservations', methods=['DELETE'])
@requires_auth('DELETE:reservation')
def delete_reservation(jwt):
    pass


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

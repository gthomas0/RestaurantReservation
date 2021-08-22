import pandas as pd
import json
from datetime import datetime, time
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sqlalchemy import exc

from .database.models import setup_db, Restaurant, Patron, Reservation, db
from .auth.auth import AuthError, requires_auth
from .utils.date_handler import get_datetime_range, get_day_column, get_day_range, get_time_range, get_weekday


app = Flask(__name__)
setup_db(app)
CORS(app)


"""
Schedule Section
"""
@app.route('/schedules', methods=['GET'])
@requires_auth('get:schedules')
def get_schedules(jwt):
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
                    open_restaurants.append({'id': restaurant.id, 'name': restaurant.name})

            return jsonify({
                'success': True,
                'restaurants': open_restaurants
            })

    except:
        abort(404)


@app.route('/schedules', methods=['POST'])
@requires_auth('post:schedules')
def post_schedules(jwt):
    try:
        if request.method == 'POST':
            if request.files:
                schedule_file = request.files['schedules']
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
            else:
                abort(422)

            return jsonify({
                'success': True
            })

    except:
        abort(422)


@app.route('/schedules', methods=['DELETE'])
@requires_auth('delete:schedules')
def delete_schedules(jwt):
    data = request.get_json(silent=True)
    id = None
    if data:
        id = data.get('id')

    try:
        if id:
            # Delete a specific schedule
            schedule = Restaurant.query.get(id)
            schedule.delete()

            return jsonify({
                'success': True,
                'delete': id
            })
        else:
            # If there is no specific schedule, delete all
            try:
                db.session.query(Restaurant).delete()
                db.session.commit()

                return jsonify({
                    'success': True,
                    'delete': 'all'
                })
            except:
                db.session.rollback()
    except:
        abort(422)


"""
Patron Section
"""
@app.route('/patrons', methods=['GET'])
@requires_auth('get:patrons')
def get_patrons(jwt):
    try:
        data = request.get_json(silent=True)
        id = None
        if data:
            id = data.get('id')
        if id:
            # If a specific patron is requested
            patron = [Patron.query.get(id)]
        else:
            # Get all if a specific patron isn't requested
            patron = Patron.query.all()
        return jsonify({
            'success': True,
            'patrons': [pat.format() for pat in patron]
        })
    except:
        abort(410)


@app.route('/patrons', methods=['POST'])
@requires_auth('post:patrons')
def post_patrons(jwt):
    try:
        if request.method == 'POST':
            body = request.get_json(silent=True)

            new_name = body.get('name')
            new_number = body.get('number')
            new_email = body.get('email')

            # if any values are missing, abort
            if not new_name or not new_number or not new_email:
                abort(422)

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


@app.route('/patrons', methods=['PATCH'])
@requires_auth('patch:patrons')
def patch_patrons(jwt):
    if request.method == 'PATCH':
        data = request.get_json(silent=True)
        id = None
        if data:
            id = data.get('id')
        patron = Patron.query.get(id)

        if patron:
            try:
                body = request.get_json(silent=True)

                new_name = body.get('name')
                new_number = body.get('number')
                new_email = body.get('email')

                if new_name:
                    patron.name = new_name
                if new_number:
                    patron.number = new_number
                if new_email:
                    patron.email = new_email
                if not new_name and not new_number and not new_email:
                    abort(422)

                patron.update()

                return jsonify({
                    'success': True,
                    'patron': patron.format()
                })
            except:
                abort(422)
        else:
            abort(404)


@app.route('/patrons', methods=['DELETE'])
@requires_auth('delete:patrons')
def delete_patrons(jwt):
    data = request.get_json(silent=True)
    id = None
    if data:
        id = data.get('id')

    try:
        if id:
            # Delete a specific schedule
            patron = Patron.query.get(id)
            patron.delete()

            return jsonify({
                'success': True,
                'delete': id
            })
        else:
            # If there is no specific schedule, delete all
            try:
                db.session.query(Patron).delete()
                db.session.commit()

                return jsonify({
                    'success': True,
                    'delete': 'all'
                })
            except:
                db.session.rollback()
    except:
        abort(422)


"""
Reservation Section
"""
@app.route('/reservations', methods=['GET'])
@requires_auth('get:reservations')
def get_reservation(jwt):
    try:
        if request.method == 'GET':
            data = list()
            reservations = db.session.query(Reservation).join(Patron).join(Restaurant).all()

            for reservation in reservations:
                rd = {
                    'restaurant_id': reservation.restaurant_id,
                    'restaurant_name': reservation.restaurant.name,
                    'patron_id': reservation.patron_id,
                    'patron_name': reservation.patron.name,
                    'start_time': reservation.start_time
                }
                data.append(rd)

        return jsonify({
            'success': True,
            'reservations': data
        })
    except:
        abort(404)


@app.route('/reservations', methods=['POST'])
@requires_auth('post:reservations')
def post_reservation(jwt):
    try:
        if request.method == 'POST':
            body = request.get_json(silent=True)

            restaurant_id = body.get('restaurant_id')
            patron_id = body.get('patron_id')
            start_time_str = body.get('start_time')
            start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S.%f')
            params = {
                'restaurant_id': restaurant_id,
                'patron_id': patron_id,
                'start_time': start_time
            }

            reservation = Reservation(**params)
            reservation.insert()

            return jsonify({
                'success': True,
                'created': reservation.format()
            })
    except:
        abort(422)


@app.route('/reservations', methods=['DELETE'])
@requires_auth('delete:reservations')
def delete_reservations(jwt):
    try:
        try:
            db.session.query(Reservation).delete()
            db.session.commit()

            return jsonify({
                'success': True,
                'delete': 'all'
            })
        except:
            db.session.rollback()
    except:
        abort(422)


## Error Handling
@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False, 
        "error": error.status_code,
        "message": error.error
    }), 401


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


@app.errorhandler(410)
def gone(error):
    return jsonify({
        "success": False,
        "error": 410,
        "message": "gone"
    }), 410

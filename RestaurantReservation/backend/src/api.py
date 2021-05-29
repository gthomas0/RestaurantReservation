import csv
from datetime import datetime
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sqlalchemy import exc

from .database.models import setup_db, Restaurant
from .auth.auth import AuthError, requires_auth
from .utils.date_handler import get_day_range, get_time_range


app = Flask(__name__)
setup_db(app)
CORS(app)



@app.route('/scedule/<datetimestr>', methods=['GET'])
#@requires_auth('get:schedule')
def get_schedule(datetimestr):
    try:
        datetime_obj = datetime.strptime(datetimestr, '%Y-%m-%d %H:%M:%S.%f')

        return jsonify({
            'success': True,
            'restaurants': restaurants
        })
    except:
        abort(404)



@app.route('/schedule', methods=['POST'])
#@requires_auth('post:schedule')
def post_schedule():
    try:
        if request.method == 'POST':
            if request.files:
                schedule_file = request.files('filenmae')
                schedule_file_string = schedule_file.read()
                schedules = [{k: v for k, v in row.items()} for row in csv.DictReader(schedule_file_string.splitlines(), skipinitialspace=True)]

                # Handle schedule upload
                for schedule in schedules:
                    times = schedule[1]
                    schedule_dict = dict()
                    for single_time in times.split('/'):
                        day_range, day_match = get_day_range(single_time)
                        time_range = get_time_range(single_time.split(day_match)[1].strip())
                        time_dict = {d: time_range for d in day_range}
                        schedule_dict.update(time_dict)

                    new_schedule = Restaurant(
                        name = schedule[0],
                        sunday = schedule_dict['Sun'],
                        monday = schedule_dict['Mon'],
                        tuesday = schedule_dict['Tues'],
                        wednesday = schedule_dict['Wed'],
                        thursday = schedule_dict['Thu'],
                        friday = schedule_dict['Fri'],
                        saturday = schedule_dict['Sat'],
                        hours = times
                    )

                    new_schedule.insert()

        return jsonify({
            'success': True,
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

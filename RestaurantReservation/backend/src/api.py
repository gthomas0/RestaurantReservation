import csv
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import setup_db, Restaurant
from .auth.auth import AuthError, requires_auth


app = Flask(__name__)
setup_db(app)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/scedule', methods=['GET'])
#@requires_auth('get:schedule')
def get_schedule():
    try:
        restaurants = Restaurant.query.all()

        return jsonify({
            'success': True,
            'restaurants': restaurants
        })
    except:
        abort(404)

"""
@app.route('/schedule', methods=['POST'])
#@requires_auth('post:schedule')
def post_schedule():
    try:
        if request.method == 'POST':
            if request.files:
                schedule_file = request.files('filenmae')
                schedule_file_string = schedule_file.read()
                csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(schedule_file_string.splitlines(), skipinitialspace=True)]

                # Handle schedule upload

        return jsonify({
            'success': True,
        })
    except:
        abort(422)
"""

@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "resource not found"
    }), 404

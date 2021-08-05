from datetime import datetime
import pathlib
import requests
import socket


HOSTNAME = socket.gethostbyname(socket.gethostname())
ADMIN_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgxMzQ3NjQsImV4cCI6MTYyODIyMTE2NCwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6InBvc3Q6c2NoZWR1bGVzIGdldDpzY2hlZHVsZXMgZGVsZXRlOnNjaGVkdWxlcyBwb3N0OnBhdHJvbnMgcGF0Y2g6cGF0cm9ucyBnZXQ6cmVzZXJ2YXRpb25zIHBvc3Q6cmVzZXJ2YXRpb25zIGdldDpwYXRyb25zIGRlbGV0ZTpwYXRyb25zIGRlbGV0ZTpyZXNlcnZhdGlvbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJwb3N0OnNjaGVkdWxlcyIsImdldDpzY2hlZHVsZXMiLCJkZWxldGU6c2NoZWR1bGVzIiwicG9zdDpwYXRyb25zIiwicGF0Y2g6cGF0cm9ucyIsImdldDpyZXNlcnZhdGlvbnMiLCJwb3N0OnJlc2VydmF0aW9ucyIsImdldDpwYXRyb25zIiwiZGVsZXRlOnBhdHJvbnMiLCJkZWxldGU6cmVzZXJ2YXRpb25zIl19.Vs0J_z7fAg8zVZpal1yax6Vep7CFM3uuwQpWYRIaUDXmvkkcHJWJqwMbEsE6XfJuKa9j7T4lSY8KwquaiYiJjV-Hao-ax82Nhh_-nsVml4BZs8aPXJVdEKobZO7_y0or5hmaRUrKvuLkJpMptD0-JYobOMaNfE9o6esFeuIiYDJkCWdaOUtJ25k3-bCsvdJbYuSKWqWb1f55K873VEYnhCqhGLlH6q8mLIX41EmXdSU1jl1ZUHaCcMo-lY6FF96oMrariYW7GRbdT3ogT3fUqt0AOxeEVpDn28PMRHtUcV5z3IODzHRNgKDSsge1hS68g7YZiWflQmj6zWmMZz0B_Q'
PATRON_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgxMjY0MTcsImV4cCI6MTYyODIxMjgxNywiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6ImdldDpzY2hlZHVsZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6c2NoZWR1bGVzIl19.UN_Mmaf8iedaZbrj3OA5teFze2RVM83jQlyATUMDx1w86GIgxCO3EedrK6YrI-CzH4I5a4dk9wIro0zLCJObAUxYTBW9X_tcV-qB7uQ4olrxov_EbQw7EFaRBpRqvkCjSuDKNkx8NqpoxqQGW3wMfV3hbMmByzsVdUz-dkNVN6ZUbT97BQhGo_90x25G8lk5c5PxBEexhB9aGOGCNn8osVHKT2Vq75QUftg40F9hTNs35MMYVOtreO71C-ec344W6GzneLWkgBygCzj4mbhG7npF_c8NHkC5927qqyX-P0rhfscI3ZKMzDlyZUQ_ADc7NTcJocJkDQ3jusLNSEchBw'

## post_schedules
def test_200_admin_add_schedules():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    file_path = pathlib.Path(__file__).parent / 'test_data' / 'test_schedule.csv'
    with open(file_path.resolve(), 'rb') as f:
        req = requests.post(
            f'http://{HOSTNAME}:5000/schedules',
            headers=headers,
            files={'schedules': f.read()}
        )
    assert req.status_code == 200
    assert req.json() == {'success': True}


def test_422_admin_add_schedules():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.post(
        f'http://{HOSTNAME}:5000/schedules',
        headers=headers
    )
    assert req.status_code == 422
    assert req.json().get('success') == False


def test_401_patron_add_schedules():
    headers = {'Authorization': f'Bearer {PATRON_TOKEN}'}
    file_path = pathlib.Path(__file__).parent / 'test_data' / 'test_schedule.csv'
    with open(file_path.resolve(), 'rb') as f:
        req = requests.post(
            f'http://{HOSTNAME}:5000/schedules',
            headers=headers,
            files={'schedules': f.read()}
        )
    assert req.status_code == 401
    assert req.json().get('success') == False


## get_schedules
def test_200_admin_get_schedules():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.get(
        f'http://{HOSTNAME}:5000/schedules',
        headers=headers,
        params={'datetimestr': '2021-05-27 12:23:53.350219'}
    )
    assert req.status_code == 200
    assert req.json().get('success') == True


def test_404_admin_get_schedules():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.get(
        f'http://{HOSTNAME}:5000/schedules',
        headers=headers,
        params={'datetimestr': '2021-05-27'}
    )
    assert req.status_code == 404
    assert req.json().get('success') == False


def test_200_patron_get_schedules():
    headers = {'Authorization': f'Bearer {PATRON_TOKEN}'}
    req = requests.get(
        f'http://{HOSTNAME}:5000/schedules',
        headers=headers,
        params={'datetimestr': '2021-05-27 12:23:53.350219'}
    )
    assert req.status_code == 200
    assert req.json().get('success') == True


def test_404_patron_get_schedules():
    headers = {'Authorization': f'Bearer {PATRON_TOKEN}'}
    req = requests.get(
        f'http://{HOSTNAME}:5000/schedules',
        headers=headers,
        params={'datetimestr': '2021-05-27'}
    )
    assert req.status_code == 404
    assert req.json().get('success') == False


## post_patrons
def test_200_admin_post_patrons():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.post(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers,
        params={
            'name': 'Greg',
            'number': '555-555-5555',
            'email': 'fake_email@gmail.com'
        }
    )
    assert req.status_code == 200
    assert req.json().get('success') == True


def test_422_admin_post_patrons():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.post(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers,
        params={
            'name': 'Greg',
            'number': '555-555-5555'
        }
    )
    assert req.status_code == 422
    assert req.json().get('success') == False


## get_patrons
def test_200_admin_get_patron():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.get(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers
    )
    assert req.status_code == 200
    assert req.json().get('success') == True


def test_410_admin_get_patron():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.get(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers,
        params={'id': -1}
    )
    assert req.status_code == 410
    assert req.json().get('success') == False


## patch_patrons
def test_200_admin_patch_patron():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}

    # Get a patron to patch
    patrons = requests.get(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers
    )
    id = patrons.json().get('patrons')[-1].get('id')
    assert patrons.json().get('patrons')[-1].get('name') == 'Greg'

    # Patch the patron
    req = requests.patch(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers,
        params={
            'id': id,
            'name': 'Joe'
        }
    )
    assert req.status_code == 200
    assert req.json().get('success') == True
    assert req.json().get('patron').get('name') == 'Joe'


def test_410_admin_patch_patron():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.patch(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers,
        params={
            'id': -1,
            'name': 'Joe'
        }
    )
    assert req.status_code == 404
    assert req.json().get('success') == False


def test_422_admin_patch_patron():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}

    # Get a patron to patch
    patrons = requests.get(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers
    )
    id = patrons.json().get('patrons')[-1].get('id')

    # Patch the patron
    req = requests.patch(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers,
        params={
            'id': id
        }
    )
    assert req.status_code == 422
    assert req.json().get('success') == False


# post_reservations
def test_200_admin_post_reservations():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}

    # Get a patron to use
    patrons = requests.get(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers
    )
    patron_id = patrons.json().get('patrons')[-1].get('id')

    # Get a restaurant to use
    restaurants = requests.get(
        f'http://{HOSTNAME}:5000/schedules',
        headers=headers,
        params={'datetimestr': '2021-05-27 12:23:53.350219'}
    )
    restaurant_id = restaurants.json().get('restaurants')[-1].get('id')

    # Post the reservation
    req = requests.post(
        f'http://{HOSTNAME}:5000/reservations',
        headers=headers,
        params={
            'restaurant_id': restaurant_id,
            'patron_id': patron_id,
            'start_time': '2021-05-27 12:23:53.350219'
        }
    )
    assert req.status_code == 200
    assert req.json() == {
        'created': {
            'restaurant_id': restaurant_id,
            'patron_id': patron_id,
            'start_time': 'Thu, 27 May 2021 12:23:53 GMT'
        },
        'success': True
    }


def test_422_admin_post_reservations():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}

    req = requests.post(
        f'http://{HOSTNAME}:5000/patrons',
        headers=headers,
        params={
            'start_time': '2021-05-27 12:23:53.350219'
        }
    )
    assert req.status_code == 422
    assert req.json().get('success') == False


## get_reservations
def test_200_admin_get_reservations():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.get(
        f'http://{HOSTNAME}:5000/reservations',
        headers=headers
    )
    assert req.status_code == 200
    assert req.json().get('success') == True


def test_401_patron_get_reservations():
    headers = {'Authorization': f'Bearer {PATRON_TOKEN}'}
    req = requests.get(f'http://{HOSTNAME}:5000/reservations', headers=headers)
    assert req.status_code == 401
    assert req.json().get('success') == False


## delete_patrons
def test_401_patron_delete_all_reservations():
    headers = {'Authorization': f'Bearer {PATRON_TOKEN}'}
    req = requests.delete(f'http://{HOSTNAME}:5000/reservations', headers=headers)
    assert req.status_code == 401
    assert req.json().get('success') == False


def test_200_admin_delete_all_reservations():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.delete(f'http://{HOSTNAME}:5000/reservations', headers=headers)
    assert req.status_code == 200
    assert req.json() == {'success': True, 'delete': 'all'}


## delete_patrons
def test_401_patron_delete_all_patrons():
    headers = {'Authorization': f'Bearer {PATRON_TOKEN}'}
    req = requests.delete(f'http://{HOSTNAME}:5000/patrons', headers=headers)
    assert req.status_code == 401
    assert req.json().get('success') == False


def test_200_admin_delete_all_patrons():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.delete(f'http://{HOSTNAME}:5000/patrons', headers=headers)
    assert req.status_code == 200
    assert req.json() == {'success': True, 'delete': 'all'}


## delete_schedules
def test_401_patron_delete_all_schedules():
    headers = {'Authorization': f'Bearer {PATRON_TOKEN}'}
    req = requests.delete(f'http://{HOSTNAME}:5000/schedules', headers=headers)
    assert req.status_code == 401
    assert req.json().get('success') == False


def test_200_admin_delete_all_schedules():
    headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
    req = requests.delete(f'http://{HOSTNAME}:5000/schedules', headers=headers)
    assert req.status_code == 200
    assert req.json() == {'success': True, 'delete': 'all'}

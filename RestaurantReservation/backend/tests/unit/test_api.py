from datetime import datetime
import pathlib
import requests
import socket


HOSTNAME = socket.gethostbyname(socket.gethostname())
ADMIN_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgyMTI2ODYsImV4cCI6MTYyODI5OTA4NiwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6InBvc3Q6c2NoZWR1bGVzIGdldDpzY2hlZHVsZXMgZGVsZXRlOnNjaGVkdWxlcyBwb3N0OnBhdHJvbnMgcGF0Y2g6cGF0cm9ucyBnZXQ6cmVzZXJ2YXRpb25zIHBvc3Q6cmVzZXJ2YXRpb25zIGdldDpwYXRyb25zIGRlbGV0ZTpwYXRyb25zIGRlbGV0ZTpyZXNlcnZhdGlvbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJwb3N0OnNjaGVkdWxlcyIsImdldDpzY2hlZHVsZXMiLCJkZWxldGU6c2NoZWR1bGVzIiwicG9zdDpwYXRyb25zIiwicGF0Y2g6cGF0cm9ucyIsImdldDpyZXNlcnZhdGlvbnMiLCJwb3N0OnJlc2VydmF0aW9ucyIsImdldDpwYXRyb25zIiwiZGVsZXRlOnBhdHJvbnMiLCJkZWxldGU6cmVzZXJ2YXRpb25zIl19.UN3j3bkdruWj-jxAxIdIhGOT-ZJbbQZoq8zv8KNKBZwZWVfb1rZKj4Iq6ME0BtFTEEtsAqO8xWDOjwWshO3G0wcK7HhCvT3bmjkcCOWPa0Ssd4KLahAAWap7ZbqTX9_vh3o6Q2GZzZMM7B3wM9EiNRejCcHbAqeMuZyT7AlRaK3BDTzJ0-4ZqeOYgfZWY5BsLlCB7DWBmImW-dk9PXYJ8Xpr72Gwg5xZ9-GS-X1cZCNdtHl__LXBhUSVb-P_PXFqbNdDpbhnVIt-VG5mzpkhtvktJVwDE3Wmjib5MnW2ln8LeQSHyKdLA3A9On0WSwN_34Yg9tkragZE3neJ1WiqxQ'
PATRON_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgyMTI3MTAsImV4cCI6MTYyODI5OTExMCwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6ImdldDpzY2hlZHVsZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6c2NoZWR1bGVzIl19.o-RC7u2hmIPA2kB4nHRHCHzYXp_M_O8rhSi-ggTGIwu8MJJcjubslK7bvxN9rFTbRRM7gSqNSYPdtlq6mKDfKo-_5bmEM4xF22UYmLJDLZJOEqvskB4r3G087XsI534XUcmmbHKpnOcJCDwGVSmsuUiSjg623OTvybhEfoVjaTWSizMejumeHQeQtCH5DQZZn6hbEjBY4X_1U5C3Jh3Nag7Oy4lUJy1jIUlN8Pbn47vPmlT2TWTq6IdTI4RaBuBAQU6o0vIThIafUuehdT8nQnjOrKHYHsTt48S-4MUrYDxKyE31ot0ElQszn87EcYiAUhNc7QIRMZxiQuJSDNAbnQ'

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
        json={
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
        json={
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
        json={'id': -1}
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
        json={
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
        json={
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
        json={
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
        json={
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
        json={
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

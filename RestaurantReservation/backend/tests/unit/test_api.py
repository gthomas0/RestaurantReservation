from datetime import datetime
import pathlib
import requests
import socket


HOSTNAME = socket.gethostbyname(socket.gethostname())
with open('README.md') as f:
    for line in f.readlines():
        if 'Admin Token:' in line:
            ADMIN_TOKEN = line.split(':')[1][2:-2]
        if 'Patron Token:' in line:
            PATRON_TOKEN = line.split(':')[1][2:-4]

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

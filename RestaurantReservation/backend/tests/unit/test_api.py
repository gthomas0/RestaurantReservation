import pathlib
import requests
import socket


HOSTNAME = socket.gethostbyname(socket.gethostname())
ADMIN_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgwNDI5OTAsImV4cCI6MTYyODEyOTM5MCwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6InBvc3Q6c2NoZWR1bGVzIGdldDpzY2hlZHVsZXMgZGVsZXRlOnNjaGVkdWxlcyBwb3N0OnBhdHJvbnMgcGF0Y2g6cGF0cm9ucyBnZXQ6cmVzZXJ2YXRpb25zIHBvc3Q6cmVzZXJ2YXRpb25zIHBhdGNoOnJlc2VydmF0aW9ucyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbInBvc3Q6c2NoZWR1bGVzIiwiZ2V0OnNjaGVkdWxlcyIsImRlbGV0ZTpzY2hlZHVsZXMiLCJwb3N0OnBhdHJvbnMiLCJwYXRjaDpwYXRyb25zIiwiZ2V0OnJlc2VydmF0aW9ucyIsInBvc3Q6cmVzZXJ2YXRpb25zIiwicGF0Y2g6cmVzZXJ2YXRpb25zIl19.J9BhbdZhrC3N85i4_1rz7nABhLfzccY1Xv8uAZwEWR39Ce3VAgUIXpxEGppE7GMRF7XyMwurnF0wL4QXSrU-vpqWvKo5_SdChluxhqXK9IVhGQFh1QuGYkfKGg1mgEWEnoMawhmU0DJ5SBKSqjwcNsM0jddJReX1OvLRybo17g_exUaedZwrBGHmX-YYI4ytD7MdWCGcE6dxm1tqy8saDHnJVzJWgzW7WRz8QxfaHxNhNLc3_drpYcA7cjXJwwT59fpzsldg0r7WXCUoKTHZ81rAUdev2BNlWrb4r-XKuSXlQhJGp2tbt8yTe_ZqfVvzfaq412sa-ldGYY2tXbqLOw'
PATRON_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InMyanZ1T01WSzlLTl9SY1l5eUxCRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3QudXMuYXV0aDAuY29tLyIsInN1YiI6IlE3VXhQMmZ6ZU9qZGtZdTY5UkxHWHdGRzRRZ2VHSkFIQGNsaWVudHMiLCJhdWQiOiJzY2hlZHVsZXIiLCJpYXQiOjE2MjgwNDY2MDIsImV4cCI6MTYyODEzMzAwMiwiYXpwIjoiUTdVeFAyZnplT2pka1l1NjlSTEdYd0ZHNFFnZUdKQUgiLCJzY29wZSI6ImdldDpzY2hlZHVsZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6c2NoZWR1bGVzIl19.WtYGSjFH4CEuy5MYqFcSM0BdRF2dbAP5T8CyGut1rRL-mf-q0re65zn6dS9JKJskg-RmMp48FpPGRGfpEvmjKzM7wLcQJbL5IfB3brZBGlUzU_d1q1IjWVtrVBhTB7yhM8z4sWv4u57IGGc0AyhW1CjvAE7zRQlPGflvutO6CHKw3mH-N9nzUxhA7chSdGl6TP-9DHLMnKhdKlSQmiLLp6Ba8-5sfRDI-K7TWtgtd4XqjtwMgdvsNvwfmhUkfCrkxPLjhfMl2wOUZlhsBtFCOxthKu9_vhQ4mTgEkN06mOjwc6JmZDbm-ZvCdHTlEZFX5_JK39INYWqMRazRTodlxw'

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
    #assert req.status_code == 422
    assert req.json().get('success') == False


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

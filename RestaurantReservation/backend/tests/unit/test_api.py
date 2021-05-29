import requests
import socket
import unittest


HOSTNAME = socket.gethostbyname(socket.gethostname())


def test_get_schedule():
    req = requests.get(f'http://{HOSTNAME}:5000/schedule')
    assert req.status_code == 200
    assert req.json() == {}

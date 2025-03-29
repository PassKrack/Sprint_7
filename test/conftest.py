from http.client import responses

import pytest
import requests
import json
from steps.courier import Courier

@pytest.fixture
def create_user():
    base_url = "https://qa-scooter.praktikum-services.ru/"
    payload = {
        "login": Courier.generate_random_string,
        "password": Courier.generate_random_string,
        "firstName": Courier.generate_random_string
    }

    requests.post(f'{base_url}api/v1/courier', data=payload)

    yield payload
    response = requests.post(f'{base_url}api/v1/courier/login', data=payload)
    params = response.json()
    requests.delete(f'{base_url}api/v1/courier/:id', data=params)




@pytest.fixture
def login(create_user):

    base_url = "https://qa-scooter.praktikum-services.ru/"
    payload = {
        "login": create_user["login"],
        "password": create_user["password"]
    }
    requests.post(f'{base_url}api/v1/courier/login', data=payload)
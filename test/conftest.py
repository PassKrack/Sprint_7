import pytest
import requests
import string
import random
import allure

@pytest.fixture(autouse=False)
def create_user():

    base_url = "https://qa-scooter.praktikum-services.ru/"
    payload = {
        "login": '',
        "password": '',
        "firstName": ''
    }
    for i in payload:
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        payload[i] = random_string

    requests.post(f'{base_url}api/v1/courier', data=payload)

    return payload

@pytest.fixture(autouse=True)
def login(create_user):

    base_url = "https://qa-scooter.praktikum-services.ru/"
    payload = {
        "login": create_user["login"],
        "password": create_user["password"]
    }
    requests.post(f'{base_url}api/v1/courier/login', data=payload)
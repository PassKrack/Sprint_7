import allure
import requests
import random
import string
from random import randint
from datetime import datetime
import datetime



class Order:

    def __init__(self, color):
        self.firstName = ''
        self.lastName = ''
        self.address = ''
        self.metroStation = ''
        self.phone = ''
        self.rentTime = ''
        self.deliveryDate = ''
        self.comment = ''
        self.color = color
        self.base_url = "https://qa-scooter.praktikum-services.ru/"


    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_digits(self, length):
        digits = string.digits
        random_digits = ''.join(random.choice(digits) for i in range(length))
        return random_digits

    def generate_date(self, date):
        date = datetime.date(2025, 6, 11)
        return date

    @allure.step('Отправить POST-запрос на создание заказа "https://qa-scooter.praktikum-services.ru/api/orders"')
    def create_order(
            self,
            firstName=None,
            lastName=None,
            address=None,
            metroStation=None,
            phone=None,
            rentTime=None,
            comment=None,
            status_code=201
    ):

        payload = {
            "firstName": self.generate_random_string(10) if not firstName else firstName,
            "lastName": self.generate_random_string(10) if not lastName else lastName,
            "address": self.generate_random_string(10) if not address else address,
            "metroStation": self.generate_random_string(10) if not metroStation else metroStation,
            "phone": self.generate_random_digits(10) if not phone else phone,
            "rentTime": randint(1,10) if not rentTime else rentTime,
            "deliveryDate": "2025-04-06",
            "comment": self.generate_random_string(10) if not comment else comment,
            "color": list(self.color)
        }

        response = requests.post(f'{self.base_url}api/v1/orders', data=payload)

        assert response.status_code == status_code, f'Код ошибки не равен ожидаемому {status_code}'
        if response.status_code == 201:
            r = response.json()
            assert 'track' in r
            payload["track"] = r["track"]
        return payload

    @allure.step(
        'Отправить GET-запрос на получение списка заказов "https://qa-scooter.praktikum-services.ru/api/orders"'
    )
    def make_list_of_orders(
            self,
            status_code=200
    ):
        payload = {
            "page": 1,
            "limit": 10
        }

        response = requests.get(f'{self.base_url}api/v1/orders', params=payload)
        assert response.status_code == status_code, f'Код ошибки не равен ожидаемому {status_code}'
        if status_code == 200:
            assert response.text is not None

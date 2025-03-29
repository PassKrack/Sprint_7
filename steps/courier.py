import allure
import requests
import random
import string

class Courier:

    def __init__(self):
        self.login = ''
        self.password = ''
        self.firsName = ''
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step(
        'Отправить POST-запрос на создание нового курьера "https://qa-scooter.praktikum-services.ru/api/v1/courier"'
    )
    def register_new_courier(
            self,
            login=None,
            password=None,
            first_name=None,
            status_code=201
        ):
        payload = {
            "login": self.generate_random_string(10) if not login else login,
            "password": self.generate_random_string(10) if not password else password,
            "firstName": self.generate_random_string(10) if not first_name else first_name
        }

        response = requests.post(f'{self.base_url}api/v1/courier', data=payload)
        assert response.status_code == status_code, f'Код ошибки не равен ожидаемому {status_code}'
        if response.status_code == 201:
            assert response.text == '{"ok":true}'
        if response.status_code == 409:
            assert  response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
        return payload

    @allure.step(
        'Отправить POST-запрос на авторизацию курьером "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"'
    )
    def login_user(self, login=None, password=None, status_code=200):
        payload = {}
        if login:
            payload["login"] = login
        if password:
            payload["password"] = password
        response = requests.post(f'{self.base_url}api/v1/courier/login', data=payload)
        assert response.status_code == status_code, f'Код ошибки не равен ожидаемому {status_code}'
        assert 'id' in response.json()

    @allure.step(
        'Отправить POST-запрос на создание курьера без поля Логин "https://qa-scooter.praktikum-services.ru/api/v1/courier"'
    )
    def register_new_courier_without_login(self,
                                           password=None,
                                           first_name=None,
                                           status_code=400
                                           ):
        payload = {
            "password": self.generate_random_string(10) if not password else password,
            "firstName": self.generate_random_string(10) if not first_name else first_name
        }
        response = requests.post(f'{self.base_url}api/v1/courier', data=payload)
        assert response.status_code == status_code, f'Код ошибки не равен ожидаемому {status_code}'
        if response.status_code == 400:
            assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    @allure.step(
        'Отправить POST-запрос на авторизацию курьером без поля Логин "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"'
    )
    def login_courier_without_login(self,
                                           password=None,
                                           status_code=400
                                           ):
        payload = {
            "password": self.generate_random_string(10) if not password else password
        }
        response = requests.post(f'{self.base_url}api/v1/courier/login', data=payload)
        assert response.status_code == status_code, f'Код ошибки не равен ожидаемому {status_code}'
        if status_code == 400:
            assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'
    @allure.step(
        'Отправить POST-запрос на авторизацию курьером с некорректной парол Логин-Пароль "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"'
    )
    def login_courier_with_incorrect_data(self,
                                           login=None,
                                           password=None,
                                           status_code=400
                                           ):
        payload = {
            "login": self.generate_random_string(10) if not login else login,
            "password": self.generate_random_string(10) if not password else password
        }
        response = requests.post(f'{self.base_url}api/v1/courier/login', data=payload)
        assert response.status_code == status_code, f'Код ошибки не равен ожидаемому {status_code}'
        if status_code == 404:
            assert response.text == '{"code":404,"message":"Учетная запись не найдена"}'

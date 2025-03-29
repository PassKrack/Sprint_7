import pytest
import allure

from steps.courier import Courier


class TestCreateCourier:

    @allure.title("Успешное создание нового курьера")
    def test_success_create_new_courier(self):
        courier = Courier()
        user = courier.register_new_courier()
        courier.login_user(
            login=user["login"],
            password=user["password"],
            status_code=200)

    @allure.title("При создании уже существующего курьера сервис возвращает ошибку")
    def test_success_duplicate_new_courier_creation_error(self):
        courier = Courier()
        user = courier.register_new_courier()
        courier.register_new_courier(
            login=user["login"],
            password=user["password"],
            first_name=user["firstName"],
            status_code=409
        )

    @allure.title("При создании нового курьера без одного из обязательных полей возвращается ошибка")
    def test_success_create_courier_without_required_field_error(self):
        courier = Courier()
        courier.register_new_courier_without_login()

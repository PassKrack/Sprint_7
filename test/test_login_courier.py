import pytest
import allure

from steps.courier import Courier


class TestLoginCourier:

    @allure.title("Успешная авторизация созданным курьером")
    def test_success_login_user(self, create_user):
        courier = Courier()
        courier.login_user(
            login=create_user["login"],
            password=create_user["password"],
            status_code=200
        )

    @allure.title("При попытке авторизации без заполнения одного из полей возвращается ошибка")
    def test_success_login_courier_without_field_error(self, create_user):
        courier = Courier()
        courier.login_courier_without_login(
            password=create_user["password"],
            status_code=400
        )

    @allure.title("При авторизации с некорректной парой логин-пароль возвращается ошибка")
    def test_success_login_courier_with_incorrect_data_error(self, create_user):
        courier = Courier()
        courier.login_courier_with_incorrect_data(
            login="Несуществующий",
            password="Пользователь",
            status_code=404
        )
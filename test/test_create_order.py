import pytest
import allure

from steps.order import Order


class TestCreateOrder:

    @allure.title("Успешное создание нового заказа")
    @pytest.mark.parametrize("color", ["BLACK", "GREY", "BLACK, GREY", ""])
    def test_success_create_order(self, login, color):
        new_order = Order(color)
        new_order.create_order()

    @allure.title("Успешное получение списка заказов")
    @pytest.mark.parametrize("color", ["BLACK"])
    def test_success_make_list_of_orders(self, login, color):
        new_order = Order(color)
        new_order.create_order()
        new_order.create_order()
        new_order.make_list_of_orders()

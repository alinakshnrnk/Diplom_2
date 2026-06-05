import allure
import pytest
from helpers.api_helpers import OrderHelper


@allure.feature("Заказы пользователя")
class TestGetUserOrders:

    @allure.title("Получить заказы для авторизованного пользователя — success")
    def test_get_orders_authorized_user(self, registered_user, ingredient_ids):
        OrderHelper.create_order(ingredient_ids, registered_user["accessToken"])

        response = OrderHelper.get_user_orders(registered_user["accessToken"])
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "orders" in body
        assert isinstance(body["orders"], list)

    @allure.title("Получить заказы для неавторизованного пользователя — 401 Unauthorized")
    def test_get_orders_unauthorized_user(self):
        response = OrderHelper.get_user_orders()
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

import allure
import pytest
from helpers.api_helpers import OrderHelper


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создать заказ с авторизацией и валидными ингредиентами — success")
    def test_create_order_with_auth_and_ingredients(self, registered_user, ingredient_ids):
        response = OrderHelper.create_order(ingredient_ids, registered_user["accessToken"])
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "order" in body
        assert "number" in body["order"]

    @allure.title("Создать заказ без авторизации, но с валидными ингредиентами — success")
    def test_create_order_without_auth_with_ingredients(self, ingredient_ids):
        response = OrderHelper.create_order(ingredient_ids)
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "order" in body

    @allure.title("Создать заказ без ингредиентов — 400 Bad Request")
    def test_create_order_without_ingredients(self, registered_user):
        response = OrderHelper.create_order([], registered_user["accessToken"])
        body = response.json()

        assert response.status_code == 400
        assert body["success"] is False
        assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Создать заказ с некорректным хэшем ингредиента — 500 Internal Server Error")
    def test_create_order_with_invalid_ingredient_hash(self, registered_user):
        response = OrderHelper.create_order(
            ["invalidhash000000000000000000000"],
            registered_user["accessToken"],
        )

        assert response.status_code == 500

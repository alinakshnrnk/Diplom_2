import allure
import pytest
from helpers.api_helpers import UserHelper
from helpers.data_generators import generate_user_data


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать уникального пользователя — success")
    def test_create_unique_user_success(self, new_user):
        response = new_user["response"]
        body = new_user["body"]
        user_data = new_user["user_data"]

        assert response.status_code == 200
        assert body["success"] is True
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == user_data["email"]

    @allure.title("Создать уже зарегистрированного пользователя — 403 Forbidden")
    def test_create_already_registered_user(self, registered_user):
        response = UserHelper.register(
            registered_user["email"],
            registered_user["password"],
            registered_user["name"],
        )
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "User already exists"

    @allure.title("Создать пользователя без email — 403 Forbidden")
    def test_create_user_without_email(self):
        user_data = generate_user_data()
        response = UserHelper.register(
            email=None,
            password=user_data["password"],
            name=user_data["name"],
        )
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"

    @allure.title("Создать пользователя без пароля — 403 Forbidden")
    def test_create_user_without_password(self):
        user_data = generate_user_data()
        response = UserHelper.register(
            email=user_data["email"],
            password=None,
            name=user_data["name"],
        )
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"

    @allure.title("Создать пользователя без имени — 403 Forbidden")
    def test_create_user_without_name(self):
        user_data = generate_user_data()
        response = UserHelper.register(
            email=user_data["email"],
            password=user_data["password"],
            name=None,
        )
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"

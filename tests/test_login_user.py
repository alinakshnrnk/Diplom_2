import allure
import pytest
from helpers.api_helpers import UserHelper


@allure.feature("Вход пользователя в систему")
class TestLoginUser:

    @allure.title("Войти с корректными учётными данными — success")
    def test_login_existing_user_success(self, registered_user):
        response = UserHelper.login(
            registered_user["email"], registered_user["password"]
        )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == registered_user["email"]

    @allure.title("Войти с некорректным email — 401 Unauthorized")
    def test_login_wrong_email(self, registered_user):
        response = UserHelper.login(
            "wrong_email@example.com", registered_user["password"]
        )
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "email or password are incorrect"

    @allure.title("Войти с некорректным паролем — 401 Unauthorized")
    def test_login_wrong_password(self, registered_user):
        response = UserHelper.login(
            registered_user["email"], "wrongpassword"
        )
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "email or password are incorrect"

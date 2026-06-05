import allure
import pytest
import uuid
from helpers.api_helpers import UserHelper


@allure.feature("Обновление пользователя")
class TestUpdateUser:

    @allure.title("Обновить email с авторизацией — success")
    def test_update_email_with_auth(self, registered_user):
        new_email = f"updated_{uuid.uuid4().hex[:6]}@example.com"
        response = UserHelper.update_user(
            registered_user["accessToken"], {"email": new_email}
        )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["email"] == new_email

    @allure.title("Обновить имя с авторизацией — success")
    def test_update_name_with_auth(self, registered_user):
        new_name = f"UpdatedName_{uuid.uuid4().hex[:6]}"
        response = UserHelper.update_user(
            registered_user["accessToken"], {"name": new_name}
        )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["name"] == new_name

    @allure.title("Обновить пароль с авторизацией — success")
    def test_update_password_with_auth(self, registered_user):
        response = UserHelper.update_user(
            registered_user["accessToken"], {"password": "NewPassword456!"}
        )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True

    @allure.title("Обновить email без авторизации — 401 Unauthorized")
    def test_update_email_without_auth(self):
        new_email = f"unauth_{uuid.uuid4().hex[:6]}@example.com"
        response = UserHelper.update_user(None, {"email": new_email})
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

    @allure.title("Обновить имя без авторизации — 401 Unauthorized")
    def test_update_name_without_auth(self):
        response = UserHelper.update_user(None, {"name": "SomeName"})
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

    @allure.title("Обновить пароль без авторизации — 401 Unauthorized")
    def test_update_password_without_auth(self):
        response = UserHelper.update_user(None, {"password": "SomePass123"})
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

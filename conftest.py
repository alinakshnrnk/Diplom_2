import pytest
from helpers.api_helpers import UserHelper, OrderHelper
from helpers.data_generators import generate_user_data


@pytest.fixture(scope="function")
def registered_user():
    user_data = generate_user_data()
    response = UserHelper.register(
        user_data["email"], user_data["password"], user_data["name"]
    )
    assert response.status_code == 200, f"Setup failed: {response.text}"
    body = response.json()
    access_token = body["accessToken"]
    refresh_token = body["refreshToken"]

    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "accessToken": access_token,
        "refreshToken": refresh_token,
    }

    UserHelper.delete(access_token)


@pytest.fixture(scope="session")
def ingredient_ids():
    response = OrderHelper.get_ingredients()
    assert response.status_code == 200
    data = response.json()["data"]
    return [item["_id"] for item in data[:2]]

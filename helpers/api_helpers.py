import requests
from config import ENDPOINTS


class UserHelper:
    @staticmethod
    def register(email, password, name):
        payload = {"email": email, "password": password, "name": name}
        return requests.post(ENDPOINTS["register"], json=payload)

    @staticmethod
    def login(email, password):
        payload = {"email": email, "password": password}
        return requests.post(ENDPOINTS["login"], json=payload)

    @staticmethod
    def delete(access_token):
        headers = {"Authorization": access_token}
        return requests.delete(ENDPOINTS["user"], headers=headers)

    @staticmethod
    def get_user(access_token):
        headers = {"Authorization": access_token}
        return requests.get(ENDPOINTS["user"], headers=headers)

    @staticmethod
    def update_user(access_token, payload):
        headers = {"Authorization": access_token}
        return requests.patch(ENDPOINTS["user"], json=payload, headers=headers)


class OrderHelper:
    @staticmethod
    def create_order(ingredient_ids, access_token=None):
        payload = {"ingredients": ingredient_ids}
        headers = {"Authorization": access_token} if access_token else {}
        return requests.post(ENDPOINTS["orders"], json=payload, headers=headers)

    @staticmethod
    def get_user_orders(access_token=None):
        headers = {"Authorization": access_token} if access_token else {}
        return requests.get(ENDPOINTS["orders"], headers=headers)

    @staticmethod
    def get_ingredients():
        return requests.get(ENDPOINTS["ingredients"])

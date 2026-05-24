BASE_URL = "https://stellarburgers.education-services.ru/api"

ENDPOINTS = {
    "register": f"{BASE_URL}/auth/register",
    "login": f"{BASE_URL}/auth/login",
    "logout": f"{BASE_URL}/auth/logout",
    "user": f"{BASE_URL}/auth/user",
    "ingredients": f"{BASE_URL}/ingredients",
    "orders": f"{BASE_URL}/orders",
    "orders_all": f"{BASE_URL}/orders/all",
}

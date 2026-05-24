import uuid


def generate_user_data():
    unique = uuid.uuid4().hex[:8]
    return {
        "email": f"test_{unique}@example.com",
        "password": "Password123!",
        "name": f"User_{unique}",
    }

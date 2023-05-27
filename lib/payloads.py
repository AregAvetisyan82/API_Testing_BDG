def valid_user_credentials(email="eve.holt@reqres.in", password="pistol"):
    user_request = {
        "email": f"{email}",
        "password": f"{password}"
    }
    return user_request

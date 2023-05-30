reqres_base = "https://reqres.in/"

register_user_reqres_in = reqres_base + "api/register"
login_user_reqres_in = reqres_base + "api/login"


def get_user_reqres_in_delay(delay):
    return reqres_base + "api/users?delay=" + f"{delay}"

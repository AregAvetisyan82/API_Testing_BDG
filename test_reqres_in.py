from lib.requests.get_requests import make_get_request
from lib.requests.post_requests import make_post_request
from test_data import testing_data
from lib import endpoints
from lib import payloads


def test_register_successful_check_id_and_token():
    data = make_post_request(endpoints.register_user_reqres_in, json_body=payloads.valid_user_credentials(),
                             status_code=200)
    user_id, auth_token = data['id'], data['token']
    assert user_id == testing_data.user_id_number, auth_token == testing_data.token


def test_login_successful_and_check_token():
    user_login = make_post_request(endpoints.login_user_reqres_in, json_body=payloads.valid_user_credentials(),
                                   status_code=200)
    token = user_login['token']
    assert token == testing_data.token


def test_delayed_response_and_check_support_url():
    delayed = make_get_request(endpoints.get_user_reqres_in_delay(testing_data.delay_time))
    delayed_support_link = delayed['support']['url']
    assert delayed_support_link == testing_data.support_url


if __name__ == '__main__':
    test_register_successful_check_id_and_token()
    test_login_successful_and_check_token()
    test_delayed_response_and_check_support_url()

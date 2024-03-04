from API_TESTING.lib.my_requests import Requests
from API_TESTING.lib import endpoints
from API_TESTING.lib.headers import header
from API_TESTING.lib.payloads import PayloadsAuthorization
from API_TESTING.testing_data.local_data import EMAIL, PASSWORD
from VmBeta.POM.lib.log_info import logger
import pytest


class TestSignInFlow(Requests, PayloadsAuthorization):
    @pytest.mark.login
    def test_login_successful(self):
        user_login = self.post_request(endpoints.login_user, header(), self.account_credentials(EMAIL, PASSWORD))
        token = user_login["data"]['token']
        logger(f"Successfully login with EMAIL: {EMAIL} and PASSWORD: {PASSWORD}.")
        with open("/Users/areg.avetisyan/PycharmProjects/BDG/Beta_ViralMango/API_TESTING/testing_data/token.txt", "w") \
                as file:
            file.write(token)

    @pytest.mark.logout
    def test_logout_successful(self):
        self.post_request(endpoints.logout_user, header(with_token=True))
        logger(f"Successfully logout from account.")

    @pytest.mark.delete
    def test_delete_user_successful(self):
        self.test_login_successful()
        self.delete_request(endpoints.delete_user, header(with_token=True))
        logger(f"Account was successfully DELETED!!!")

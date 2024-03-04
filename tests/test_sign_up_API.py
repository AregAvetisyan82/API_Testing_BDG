from API_TESTING.lib.my_requests import Requests
from API_TESTING.lib import endpoints
from API_TESTING.lib.headers import header
from API_TESTING.lib.payloads import PayloadsAuthorization, PayloadsSocialPlatforms
from API_TESTING.testing_data.local_data import HANDLE, EMAIL, PASSWORD, INSTAGRAM, TIKTOK, YOUTUBE, \
    EXISTING_HANDLE, INVALID_HANDLE, ERROR_MESSAGE_INVALID, ERROR_MESSAGE_EXISTING
from VmBeta.POM.lib.log_info import logger
import pytest


class TestSignUpFlow(Requests, PayloadsAuthorization, PayloadsSocialPlatforms):
    @pytest.mark.success_sign_up
    def test_reg_step1_for_user_handle_availability_valid(self):
        user_handle = self.post_request(endpoints.check_user_handle_availability(HANDLE), header())
        message = user_handle['message']
        assert message == "success"

    @pytest.mark.success_sign_up_other
    def test_reg_step1_for_user_handle_availability_existing(self):
        user_handle = self.post_request(endpoints.check_user_handle_availability(EXISTING_HANDLE), header(),
                                        status_code=422)
        message = user_handle['message']
        assert message == ERROR_MESSAGE_EXISTING

    @pytest.mark.success_sign_up_other
    def test_reg_step1_for_user_handle_availability_invalid(self):
        user_handle = self.post_request(endpoints.check_user_handle_availability(INVALID_HANDLE), header(),
                                        status_code=422)
        message = user_handle['message']
        assert message == ERROR_MESSAGE_INVALID

    @pytest.mark.success_sign_up
    def test_reg_step2_for_user_registration(self):
        user_registered = self.post_request(endpoints.reg_step2, header(),
                                            self.account_credentials(EMAIL, PASSWORD, HANDLE))
        logger(f"Successfully registered with EMAIL: {EMAIL} and PASSWORD: {PASSWORD}.")
        token = user_registered["data"]['token']
        with open("/Users/areg.avetisyan/PycharmProjects/BDG/Beta_ViralMango/API_TESTING/testing_data/token.txt", "w") \
                as file:
            file.write(token)

    @pytest.mark.success_sign_up
    def test_reg_step3_for_user_registration(self):
        user_registered = self.post_request(endpoints.reg_step3, header(with_token=True),
                                            self.social_platform_accounts(INSTAGRAM, TIKTOK, YOUTUBE))
        message = user_registered['message']
        assert message == "Success"

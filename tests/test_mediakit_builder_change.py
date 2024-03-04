from API_TESTING.lib.my_requests import Requests
from API_TESTING.lib import endpoints
from API_TESTING.lib.headers import header
from API_TESTING.lib.payloads import PayloadsBasicElements, PayloadsSystemProfile, ImageUpload
from API_TESTING.tests.test_mediakit_builder_create import TestCreateMediakit
from API_TESTING.testing_data.local_data import IMAGE_NAME, IMAGE_PATH, BIO, CTA, NAME, AVATAR_SHAPE, TITLE, CURRENCY, \
    RATES
from VmBeta.POM.lib.log_info import logger
import pytest
import os
import requests


class TestMediaKitChanges(Requests, PayloadsBasicElements, PayloadsSystemProfile, ImageUpload):
    create = TestCreateMediakit()

    @pytest.mark.system_profile
    @pytest.mark.front
    def test_change_mediakit_system_profile(self):
        country = self.create.test_countries_request()
        categories = self.create.test_categories_request()
        self.put_request(endpoints.add_slug_for_mediakit_changes(), header(with_token=True),
                         self.system_profile_credentials(avatar_shape=AVATAR_SHAPE[0], name=NAME, country=country,
                                                         categories=categories, cta=CTA, bio=BIO))

    @pytest.mark.system_profile
    @pytest.mark.front
    def test_change_mediakit_upload_avatar(self):
        data = self.post_request(endpoints.add_slug_for_mediakit_changes(upload_avatar=True), header(with_token=True),
                                 file=self.upload_image(IMAGE_NAME, IMAGE_PATH))
        result = data['data']['image']
        logger(f"Uploaded avatar image INGO is: {result}.")

    @pytest.mark.upload_image
    def test_change_mediakit_upload_image(self):
        data = self.post_request(endpoints.add_slug_for_mediakit_changes(uplaod_image=True), header(with_token=True),
                                 file=self.upload_image(IMAGE_NAME, IMAGE_PATH))
        result = data['data']['image']
        logger(f"Uploaded Image Component INFO is: {result}.")
        return result

    @pytest.mark.image_component
    @pytest.mark.front
    def test_change_mediakit_image_component(self):
        image_url = self.test_change_mediakit_upload_image()
        self.put_request(endpoints.add_slug_for_mediakit_changes(), header(with_token=True, json_content=True),
                         self.image_credentials(image_url=image_url))

    @pytest.mark.upload_background_image
    def test_upload_mediakit_background_image(self):
        data = self.post_request(endpoints.add_slug_for_mediakit_changes(uplaod_background=True),
                                 header(with_token=True), file=self.upload_image(IMAGE_NAME, IMAGE_PATH))
        result = data['data']['image']
        logger(f"Uploaded Background Image INFO is: {result}.")
        return result

    @pytest.mark.change_background_image
    def test_change_mediakit_background_image(self):
        bg_image = self.test_upload_mediakit_background_image()
        self.put_request(endpoints.add_slug_for_mediakit_changes(), header(with_token=True),
                         self.background_image(bg_image=bg_image))

    @pytest.mark.change_background_image_unsplash
    def test_change_mediakit_background_image(self):
        bg_image = self.create.test_unsplash_images_request(image_name='icon')
        self.put_request(endpoints.add_slug_for_mediakit_changes(), header(with_token=True),
                         self.background_image(bg_image=bg_image[9]['image']))

    @pytest.mark.service_list
    def test_change_mediakit_service_list(self):
        data = self.put_request(endpoints.add_slug_for_mediakit_changes(), header(with_token=True), self.service_list_credentials(uid="service_list_+_0", title=TITLE, currency=CURRENCY, rate=RATES, rates_number=1, d_h=10))
        result = data[1]['data']['mediakit']['content']['components']
        a = result[0]['service_list']
        for i in range(len(a)):
            logger(f"Response Code is:{data[0]}.")
            logger(f"Service Lists {i+1} element: {result[0]['service_list'][i]['title']} - "
                   f"{result[0]['service_list'][i]['rate']}"
                   f" {result[0]['service_list'][i]['currency']}")

    @pytest.mark.service_list1
    def test_change_mediakit_service_list1(self):
        data = self.put_request(endpoints.add_slug_for_mediakit_changes(), header(with_token=True, json_content=True), self.service_list_credentials(uid="service_list_+_1", title=TITLE, currency=CURRENCY, rate=RATES, rates_number=6), json_content=True)
        logger(f"Response Code is:{data[0]} and error message: {data[1]['message']}")

    @pytest.mark.fonts
    def test_change_mediakit_fonts(self):
        font_groups = []
        components = self.create.test_components_request()
        for i in components['font-groups']:
            font_groups.append(i)
        for i in font_groups:
            dir_name = f"/Users/areg.avetisyan/Desktop/Fonts/{components['font-groups'][i]['order']}"
            os.mkdir(dir_name)
            image = components['font-groups'][i]['image']
            image_name = f"{components['font-groups'][i]['order']}.jpg"
            response = requests.get(image)
            with open(f"{dir_name}/{image_name}", "wb") as f:
                f.write(response.content)
                font1 = components['font-groups'][i]['1']['link']
                font2 = components['font-groups'][i]['2']['link']
                font3 = components['font-groups'][i]['3']['link']
            response1 = requests.get(font1)
            response2 = requests.get(font2)
            response3 = requests.get(font3)
            family_name1 = components['font-groups'][i]['1']['family_name']
            family_name2 = components['font-groups'][i]['2']['family_name']
            family_name3 = components['font-groups'][i]['3']['family_name']
            variant1 = components['font-groups'][i]['1']['variant']
            variant2 = components['font-groups'][i]['2']['variant']
            variant3 = components['font-groups'][i]['3']['variant']
            with open(f"{dir_name}/1-{family_name1}-{variant1}.otf", "wb") as f:
                f.write(response1.content)
            with open(f"{dir_name}/2-{family_name2}-{variant2}.otf", "wb") as f:
                f.write(response2.content)
            with open(f"{dir_name}/3-{family_name3}-{variant3}.otf", "wb") as f:
                f.write(response3.content)

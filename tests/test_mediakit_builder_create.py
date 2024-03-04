from API_TESTING.lib.my_requests import Requests
from API_TESTING.lib import endpoints
from API_TESTING.lib.headers import header
from VmBeta.POM.lib.log_info import logger
import pytest
import json
from API_TESTING.testing_data.local_data import COUNTRY, CATEGORIES


class TestCreateMediakit(Requests):
    @pytest.mark.my_info
    def test_me_info_request(self):
        data = self.get_request(endpoints.me_info, header(with_token=True))
        return data['data']['user']

    @pytest.mark.show_info
    def test_show_info_request(self):
        data = self.get_request(endpoints.add_slug_for_mediakit_changes(), header(with_token=True))
        return data['data']['mediakit']

    @pytest.mark.slugs
    def test_list_of_mediakits_request(self):
        data = self.get_request(endpoints.list_info, header(with_token=True))
        return data['data']['mediakits']

    @pytest.mark.colors
    def test_theme_colors_info_request(self):
        data = self.get_request(endpoints.theme_colors, header(with_token=True))
        return data['data']['colors']

    @pytest.mark.components
    def test_components_request(self):
        data = self.get_request(endpoints.get_components(), header(with_token=True))
        return data['data']

    @pytest.mark.countries
    def test_countries_request(self):
        data = self.get_request(url=endpoints.get_countries(), header=header(with_token=True))
        countries = data['data']['countries']
        for i in countries:
            if i['name'] == COUNTRY:
                logger(f"COUNTRY: {i['name']}.")
                return i['name']
        return ""

    @pytest.mark.categories
    def test_categories_request(self):
        data = self.get_request(url=endpoints.get_categories(), header=header(with_token=True))
        categories = data['data']['categories']
        a = ""
        for i in categories:
            if str(i['id']) in CATEGORIES:
                a += f"{i['id']}, "
        return a[:-2]

    @pytest.mark.unsplash_images
    def test_unsplash_images_request(self, image_name=""):
        data = self.get_request(url=endpoints.get_unsplash(search=True, image_name=image_name), header=header(with_token=True))
        return data['data']['images']

    @pytest.mark.create
    def test_create_mediakit(self):
        data = self.post_request(endpoints.list_info, header(with_token=True))
        slug = data['data']['mediakit']['slug']
        logger(f"My created MediaKit`s HANDLE is: {slug}.")
        with open("/Users/areg.avetisyan/PycharmProjects/BDG/Beta_ViralMango/API_TESTING/testing_data/slug.txt", "w") \
                as file:
            file.write(slug)
        mediakit = json.dumps(data['data']['mediakit'])
        with open("/Users/areg.avetisyan/PycharmProjects/BDG/Beta_ViralMango/API_TESTING/testing_data/mkit.json", "w") \
                as file:
            file.write(mediakit)

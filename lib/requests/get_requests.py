import requests
import json


def make_get_request(url="", status_code=200):
    response = requests.get(url)
    assert response.status_code == status_code
    return json.loads(response.text)

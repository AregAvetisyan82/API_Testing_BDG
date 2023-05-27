import requests


def make_delete_request(url="", status_code=204):
    response = requests.delete(url)
    assert response.status_code == status_code
    return response.text

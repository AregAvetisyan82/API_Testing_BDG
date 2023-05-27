import requests
import json


def make_put_request(url="", header="", json_body="", status_code=200):
    json.dumps(json_body)
    response = requests.put(url, json=json_body, headers=header)
    assert response.status_code == status_code
    return json.loads(response.text)

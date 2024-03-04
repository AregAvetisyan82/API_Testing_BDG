import requests
import json


class Requests:
    def get_request(self, url, header, status_code=200):
        response = requests.get(url, headers=header)
        assert response.status_code == status_code
        return json.loads(response.text)

    def post_request(self, url, header, payload="", file="", status_code=200, json_content=False):
        if json_content:
            json.dumps(payload)
        response = requests.post(url, headers=header, data=payload, files=file)
        assert response.status_code == status_code
        return json.loads(response.text)

    def put_request(self, url, header, payload, file="", status_code=200, json_content=False):
        if json_content:
            json.dumps(payload)
        response = requests.put(url, headers=header, data=payload, files=file)
        assert response.status_code == status_code
        return json.loads(response.text)

    def delete_request(self, url, header, status_code=200):
        response = requests.delete(url, headers=header)
        assert response.status_code == status_code
        return response.text

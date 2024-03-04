def header(json_content=False, with_token=False):
    if json_content:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        return headers
    if with_token:
        with open("/Users/areg.avetisyan/PycharmProjects/BDG/Beta_ViralMango/API_TESTING/testing_data/token.txt", "r") \
                as file:
            token = file.read()
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        return headers
    if json_content and with_token:
        with open("/Users/areg.avetisyan/PycharmProjects/BDG/Beta_ViralMango/API_TESTING/testing_data/token.txt", "r") \
                as file:
            token = file.read()
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        return headers
    headers = {
        'Accept': 'application/json'
    }
    return headers

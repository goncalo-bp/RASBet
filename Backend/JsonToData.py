import requests
import DBQueries
import DBConstants

class JsonToData:

    headers = {
        'accept': 'application/json',
    }
    api_url = "http://ucras.di.uminho.pt/v1/games/"
    response = requests.get(api_url, headers=headers)
    data = response.json()
    headers = response.headers


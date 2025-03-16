import settings
import courier
import requests

order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

create_order_url = settings.APP_URL + settings.ORDER_CREATE

def create_order():
    respons = requests.post(create_order_url, json = order_data)
    return respons.json()
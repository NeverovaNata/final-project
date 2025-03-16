import settings
import courier
import orders
import requests

courier_create_url = settings.APP_URL + settings.COURIER_CREATE
take_order_url = settings.APP_URL + settings.ORDER_CHECK

def test_courier_login(url):
    answer = courier.create_courier(url)
    if "ok" in answer:
        print("Курьер создан")
    else:
        print("Курьер уже был создан ранее")

def test_created_order_by_track():
    test_courier_login(courier_create_url)
    track = orders.create_order()['track']
    url = take_order_url + str(track)
    pull_order = requests.get(url)
    assert pull_order.status_code == 200, f"Expected status code 200, but got {pull_order.status_code}"

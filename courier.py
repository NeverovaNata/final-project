# Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
# Клиент создает заказ.
# Проверяется, что по треку заказа можно получить данные о заказе.
# Шаги автотеста:
# Выполнить запрос на создание заказа.
# Сохранить номер трека заказа.
# Выполнить запрос на получения заказа по треку заказа.
# Проверить, что код ответа равен 200.

import requests
import settings

url = settings.APP_URL + settings.COURIER_CREATE

def create_courier(url):
    create_res = requests.post(url, json = settings.courier_data)
    return(create_res.text)
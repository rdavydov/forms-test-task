# скрипт, который совершает тестовые запросы

import requests

url = 'http://127.0.0.1:5000/get_form'
data = {
    'field_name_1': 'test@test.ru',
    'field_name_2': '+7 123 456 78 90'}

response = requests.post(url, data=data)
print(response.text)

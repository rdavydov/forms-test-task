# скрипт, который совершает тестовые запросы
# должен вернуть UserForm, так как посылаем почту и телефон

import requests

url = 'http://127.0.0.1:5000/get_form'
data = {
    'field_email': 'test@test.ru',
    'field_phone': '+7 123 456 78 90'
}

response = requests.post(url, data=data)
print(response.text)

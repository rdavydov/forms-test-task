# скрипт, который совершает тестовые запросы
# должен вернуть OrderForm, так как посылаем текст и дату

import requests

url = 'http://127.0.0.1:5000/get_form'
data = {
    'field_text': 'Test Item',
    'field_date': '2023-11-15'
}

response = requests.post(url, data=data)
print(response.text)

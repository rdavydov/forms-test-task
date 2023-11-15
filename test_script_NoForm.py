# скрипт, который совершает тестовые запросы
# должен вернуть результат динамической типизации полей, так как шаблон формы не матчится
# обратите внимание на то, что дата матчится как текст, а не date, так как разделитель / вместо .

import requests

url = 'http://127.0.0.1:5000/get_form'
data = {
    'field_date': '15/11/2023',
    'field_email': 'test1@test1.ru',
}

response = requests.post(url, data=data)
print(response.text)

from tinydb import TinyDB

# Создаем объект базы данных TinyDB и записываем в него тестовые данные
db = TinyDB('database.json')

# Вставляем первую запись с именем "UserForm" и двумя полями: "email" и "phone"
db.insert({
    "form_name": "UserForm",
    "field_email": "email",
    "field_phone": "phone"
})

# Вставляем вторую запись с именем "OrderForm" и двумя полями: "text" и "date"
db.insert({
    "form_name": "OrderForm",
    "field_text": "text",
    "field_date": "date"
})

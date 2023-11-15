from tinydb import TinyDB

# Создаем объект базы данных TinyDB и записываем в него тестовые данные
db = TinyDB('database.json')

# Вставляем первую запись с именем "MyForm" и двумя полями: "email" и "phone"
db.insert({
    "name": "MyForm",
    "field_name_1": "email",
    "field_name_2": "phone"
})

# Вставляем вторую запись с именем "OrderForm" и двумя полями: "text" и "date"
db.insert({
    "name": "OrderForm",
    "field_name_1": "text",
    "field_name_2": "date"
})

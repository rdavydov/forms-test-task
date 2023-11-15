from flask import Flask, request, jsonify
from tinydb import TinyDB
import datetime

# Создаем объект Flask
app = Flask(__name__)

# Инициализируем базу данных TinyDB
db = TinyDB('database.json')

# Обработчик POST-запросов по адресу '/get_form'
@app.route('/get_form', methods=['POST'])
def get_form():
    # Получаем данные формы из тела POST-запроса
    form_data = request.form

    # Выводим текст запроса в консоль Flask
    print("Received form data:", form_data)

    # Пытаемся найти соответствующий шаблон в базе данных
    template_name = find_matching_template(form_data)
    
    # Если шаблон найден, возвращаем его имя
    if template_name:
        return template_name
    # Если шаблон не найден, производим динамическую типизацию полей и возвращаем результат
    else:
        return jsonify(perform_dynamic_typing(form_data))

# Функция поиска соответствующего шаблона в базе данных
def find_matching_template(form_data):
    # Получаем все шаблоны из базы данных
    templates = db.all()
    
    # Проходимся по каждому шаблону
    for template in templates:
        # Получаем список полей шаблона и формы
        template_fields = set(template.keys()) - {'form_name'}
        form_fields = set(form_data.keys())
        
        # Проверяем, что все поля шаблона присутствуют в форме
        if template_fields.issubset(form_fields):
            # Проверяем, что значения полей совпадают и проходят валидацию
            matching = all(form_data[field] and validate_field(form_data[field], template[field]) for field in template_fields)
            
            # Если совпадение найдено, возвращаем имя шаблона
            if matching:
                return template['form_name']
    
    # Если совпадение не найдено, возвращаем None
    return None

# Функция валидации значений полей
def validate_field(value, field_type):
    if field_type == 'email':
        # Проверка, что значение соответствует формату email
        if '@' in value and '.' in value:
            return True
        else:
            return False
    elif field_type == 'phone':
        value = value.replace(' ', '')
        # Проверка, что значение соответствует формату телефона
        if (
            ((value.startswith('+7') and len(value) == 12) or ((value.startswith('7') or value.startswith('8')) and len(value) == 11))
            and value.isdigit()
        ):
            return True
        else:
            return False
    elif field_type == 'date':
        # Проверка, что значение соответствует формату DD.MM.YYYY или YYYY-MM-DD
        try:
            if '-' in value:
                datetime.datetime.strptime(value, '%Y-%m-%d')
            else:
                datetime.datetime.strptime(value, '%d.%m.%Y')
            return True
        except ValueError:
            return False
    elif field_type == 'text':
        # Проверка, что текстовое поле не пустое
        return bool(value.strip())
    else:
        # Если указан неизвестный тип поля, считаем его валидным
        return True

# Функция динамической типизации полей
def perform_dynamic_typing(form_data):
    field_types = {}
    priority_order = ['date', 'phone', 'email', 'text']

    # Проходимся по каждому полю формы
    for field_name, value in form_data.items():
        # Проходим по порядку приоритета типов полей
        for field_type in priority_order:
            # Если поле проходит валидацию для текущего типа, добавляем его в результат
            if validate_field(value, field_type):
                field_types[field_name] = field_type
                break

    # Возвращаем результат динамической типизации
    return field_types

# запускаем Flask-приложение
if __name__ == '__main__':
    app.run(debug=True)

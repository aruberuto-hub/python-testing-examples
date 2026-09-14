"""
validate_input.py

Функция проверки строки на валидность ввода в формате:
"Имя, Возраст, Город проживания"

Пример валидной строки: "Семён, 22, Москва"
"""

import re

NAME_PATTERN = re.compile(r"^[A-ZА-ЯЁ][a-zа-яё-]*$")
CITY_PATTERN = re.compile(r"^[A-ZА-ЯЁ][a-zа-яё]*([\s-][A-ZА-ЯЁ][a-zа-яё]*)*$")

MIN_AGE = 0
MAX_AGE = 150


def is_valid_input(raw: str) -> bool:
    """
    Проверяет, что строка соответствует формату "Имя, Возраст, Город".

    Правила:
    - Ровно три поля, разделённые запятой
    - Имя: непустое, только буквы и дефис, начинается с заглавной буквы
    - Возраст: целое число в диапазоне 0-150
    - Город: непустое, только буквы, дефис и пробел, начинается с заглавной буквы
    """
    if raw is None:
        return False

    parts = raw.split(",")
    if len(parts) != 3:
        return False

    name, age_raw, city = (part.strip() for part in parts)

    if not name or not NAME_PATTERN.match(name):
        return False

    if not city or not CITY_PATTERN.match(city):
        return False

    if not age_raw.isdigit():
        return False

    age = int(age_raw)
    if age < MIN_AGE or age > MAX_AGE:
        return False

    return True

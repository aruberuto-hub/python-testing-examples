"""
test_validate_input.py

Юнит-тесты для функции is_valid_input (validate_input.py).
Запуск: pytest test_validate_input.py -v
"""

import pytest
from validate_input import is_valid_input


def test_valid_input_passes():
    assert is_valid_input("Семён, 22, Москва") is True


def test_valid_input_with_hyphenated_city():
    assert is_valid_input("Анна, 30, Санкт-Петербург") is True


def test_missing_field_fails():
    # Только два поля вместо трёх
    assert is_valid_input("Семён, 22") is False


def test_extra_field_fails():
    # Четыре поля вместо трёх
    assert is_valid_input("Семён, 22, Москва, Россия") is False


def test_non_numeric_age_fails():
    assert is_valid_input("Семён, двадцать два, Москва") is False


@pytest.mark.parametrize("age", ["-5", "151", "-1", "1000"])
def test_age_out_of_range_fails(age):
    assert is_valid_input(f"Семён, {age}, Москва") is False


def test_empty_name_fails():
    assert is_valid_input(", 22, Москва") is False


def test_lowercase_name_fails():
    # Имя должно начинаться с заглавной буквы
    assert is_valid_input("семён, 22, Москва") is False


def test_extra_whitespace_is_tolerated():
    # Пробелы вокруг полей не должны ломать валидацию
    assert is_valid_input("  Семён ,  22 , Москва  ") is True

import random
import string
from datetime import datetime, timedelta


def generate_random_string(length=10):
    """Строка из букв нижнего регистра"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_courier_payload():
    """Данные нового уникального курьера"""
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }


def get_date_in(days):
    """Дата через N дней в формате ГГГГ-ММ-ДД"""
    return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
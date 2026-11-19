import allure
import requests

from data.config import BASE_URL, COURIER_ENDPOINT, LOGIN_ENDPOINT


class CourierApi:

    @staticmethod
    @allure.step("Создать курьера")
    def create(payload):
        return requests.post(BASE_URL + COURIER_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Авторизовать курьера")
    def login(payload):
        return requests.post(BASE_URL + LOGIN_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Удалить курьера")
    def delete(courier_id):
        return requests.delete(f"{BASE_URL}{COURIER_ENDPOINT}/{courier_id}")
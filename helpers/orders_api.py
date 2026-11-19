import allure
import requests

from data.config import BASE_URL, ORDERS_ENDPOINT


class OrdersApi:

    @staticmethod
    @allure.step("Создать заказ")
    def create(payload):
        return requests.post(BASE_URL + ORDERS_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Получить список заказов")
    def get_list():
        return requests.get(BASE_URL + ORDERS_ENDPOINT)

    @staticmethod
    @allure.step("Отменить заказ")
    def cancel(track):
        return requests.put(f"{BASE_URL}{ORDERS_ENDPOINT}/cancel", json={"track": track})
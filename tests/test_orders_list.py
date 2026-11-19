import allure

from helpers.orders_api import OrdersApi


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В тело ответа возвращается список заказов")
    def test_get_orders_returns_list(self):
        response = OrdersApi.get_list()

        assert isinstance(response.json()["orders"], list)
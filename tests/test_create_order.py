import allure
import pytest

from data.order_data import ORDER_COLOR_IDS, ORDER_COLORS, build_order_payload
from helpers.orders_api import OrdersApi


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ создаётся с любым выбором цвета: код ответа 201")
    @pytest.mark.parametrize("color", ORDER_COLORS, ids=ORDER_COLOR_IDS)
    def test_create_order_returns_201(self, color, created_orders):
        response = OrdersApi.create(build_order_payload(color))
        created_orders.append(response.json().get("track"))

        assert response.status_code == 201

    @allure.title("Тело ответа при создании заказа содержит track")
    @pytest.mark.parametrize("color", ORDER_COLORS, ids=ORDER_COLOR_IDS)
    def test_create_order_returns_track(self, color, created_orders):
        response = OrdersApi.create(build_order_payload(color))
        created_orders.append(response.json().get("track"))

        assert "track" in response.json()
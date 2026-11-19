import pytest

from helpers.courier_api import CourierApi
from helpers.generators import generate_courier_payload
from helpers.orders_api import OrdersApi


@pytest.fixture
def courier_payload():
    """Данные нового курьера. После теста курьер удаляется, если был создан"""
    payload = generate_courier_payload()
    yield payload

    response = CourierApi.login({"login": payload["login"], "password": payload["password"]})
    if response.status_code == 200:
        CourierApi.delete(response.json()["id"])


@pytest.fixture
def registered_courier(courier_payload):
    """Уже созданный курьер"""
    CourierApi.create(courier_payload)
    return courier_payload


@pytest.fixture
def created_orders():
    """Список track созданных в тесте заказов. После теста заказы отменяются"""
    tracks = []
    yield tracks

    for track in tracks:
        OrdersApi.cancel(track)
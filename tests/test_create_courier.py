import allure
import pytest

from data.messages import CREATE_COURIER_NOT_ENOUGH_DATA, LOGIN_ALREADY_USED
from helpers.courier_api import CourierApi
from helpers.generators import generate_random_string


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать: код ответа 201")
    def test_create_courier_returns_201(self, courier_payload):
        response = CourierApi.create(courier_payload)

        assert response.status_code == 201

    @allure.title("Успешное создание курьера возвращает ok: true")
    def test_create_courier_returns_ok_true(self, courier_payload):
        response = CourierApi.create(courier_payload)

        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров: код ответа 409")
    def test_create_duplicate_courier_returns_409(self, registered_courier):
        response = CourierApi.create(registered_courier)

        assert response.status_code == 409

    @allure.title("Нельзя создать курьера с уже существующим логином: код ответа 409")
    def test_create_courier_with_existing_login_returns_409(self, registered_courier):
        payload = {**registered_courier, "password": generate_random_string()}
        response = CourierApi.create(payload)

        assert response.status_code == 409

    @allure.title("Создание курьера с существующим логином возвращает сообщение об ошибке")
    def test_create_courier_with_existing_login_returns_message(self, registered_courier):
        response = CourierApi.create(registered_courier)

        assert response.json()["message"] == LOGIN_ALREADY_USED

    @allure.title("Без обязательного поля курьер не создаётся: код ответа 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_400(self, courier_payload, missing_field):
        payload = {k: v for k, v in courier_payload.items() if k != missing_field}
        response = CourierApi.create(payload)

        assert response.status_code == 400

    @allure.title("Без обязательного поля возвращается сообщение об ошибке")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_message(self, courier_payload, missing_field):
        payload = {k: v for k, v in courier_payload.items() if k != missing_field}
        response = CourierApi.create(payload)

        assert response.json()["message"] == CREATE_COURIER_NOT_ENOUGH_DATA
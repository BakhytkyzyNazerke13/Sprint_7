import allure
import pytest

from data.messages import ACCOUNT_NOT_FOUND, LOGIN_NOT_ENOUGH_DATA
from helpers.courier_api import CourierApi
from helpers.generators import generate_random_string


def credentials(courier):
    """Только логин и пароль (без имени) для авторизации"""
    return {"login": courier["login"], "password": courier["password"]}


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться: код ответа 200")
    def test_login_courier_returns_200(self, registered_courier):
        response = CourierApi.login(credentials(registered_courier))

        assert response.status_code == 200

    @allure.title("Успешная авторизация возвращает id")
    def test_login_courier_returns_id(self, registered_courier):
        response = CourierApi.login(credentials(registered_courier))

        assert isinstance(response.json().get("id"), int)

    @allure.title("Без обязательного поля авторизация не проходит")
    @pytest.mark.parametrize(
        "missing_field, expected_code",
        [("login", 400), ("password", 504)],  # без password сервис реально отвечает 504
        ids=["без login", "без password"],
    )
    def test_login_without_required_field_returns_error_code(self, registered_courier, missing_field, expected_code):
        payload = {k: v for k, v in credentials(registered_courier).items() if k != missing_field}
        response = CourierApi.login(payload)

        assert response.status_code == expected_code

    @allure.title("Без login возвращается сообщение об ошибке")
    def test_login_without_login_returns_message(self, registered_courier):
        payload = {"password": registered_courier["password"]}
        response = CourierApi.login(payload)

        assert response.json()["message"] == LOGIN_NOT_ENOUGH_DATA

    @allure.title("Неверный пароль: код ответа 404")
    def test_login_with_wrong_password_returns_404(self, registered_courier):
        payload = {**credentials(registered_courier), "password": generate_random_string()}
        response = CourierApi.login(payload)

        assert response.status_code == 404

    @allure.title("Неверный логин: код ответа 404")
    def test_login_with_wrong_login_returns_404(self, registered_courier):
        payload = {**credentials(registered_courier), "login": generate_random_string()}
        response = CourierApi.login(payload)

        assert response.status_code == 404

    @allure.title("Несуществующий пользователь: код ответа 404")
    def test_login_nonexistent_user_returns_404(self, courier_payload):
        response = CourierApi.login(credentials(courier_payload))

        assert response.status_code == 404

    @allure.title("Несуществующий пользователь: возвращается сообщение об ошибке")
    def test_login_nonexistent_user_returns_message(self, courier_payload):
        response = CourierApi.login(credentials(courier_payload))

        assert response.json()["message"] == ACCOUNT_NOT_FOUND
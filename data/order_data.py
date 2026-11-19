from helpers.generators import get_date_in

# None означает, что поле color не передаётся совсем
ORDER_COLORS = [["BLACK"], ["GREY"], ["BLACK", "GREY"], None]
ORDER_COLOR_IDS = ["BLACK", "GREY", "BLACK и GREY", "без цвета"]


def build_order_payload(color):
    payload = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Пушкина, д. 10",
        "metroStation": 4,
        "phone": "+79991112233",
        "rentTime": 5,
        "deliveryDate": get_date_in(3),
        "comment": "Позвонить за час до доставки",
    }
    if color is not None:
        payload["color"] = color
    return payload
# Sprint_7

Автотесты для API учебного сервиса «Яндекс Самокат».

## Что проверяется
- Создание курьера
- Логин курьера
- Создание заказа
- Список заказов

## Установка
```bash
pip install -r requirements.txt
```

## Запуск тестов
```bash
pytest tests/ -v
```

## Allure-отчёт

```bash
pytest tests/ --alluredir=allure_results
allure generate allure_results -o allure_report --clean
allure open allure_report
```

## Структура

```text 
Sprint_7/
├── data/                          # Данные: константы, тексты, тестовые данные
│   ├── __init__.py                # Пустой файл, чтобы Python видел папку как пакет
│   ├── config.py                  # Адрес сервиса (BASE_URL) и пути ручек API
│   ├── messages.py                # Ожидаемые тексты ошибок
│   └── order_data.py              # Данные заказа и варианты цвета (параметры для тестов)
│
├── helpers/                       # Вспомогательный код: запросы к API и генераторы
│   ├── __init__.py                # Пустой файл
│   ├── generators.py              # Случайные строки, данные нового курьера, дата для заказа
│   ├── courier_api.py             # Запросы по курьеру: создать, войти, удалить
│   └── orders_api.py              # Запросы по заказам: создать, получить список, отменить
│
├── tests/                         # Только тесты, по одному файлу на ручку
│   ├── __init__.py                # Пустой файл
│   ├── test_create_courier.py     # Класс TestCreateCourier: ручка «Создать курьера»
│   ├── test_login_courier.py      # Класс TestLoginCourier: ручка «Логин курьера»
│   ├── test_create_order.py       # Класс TestCreateOrder: ручка «Создать заказ»
│   └── test_orders_list.py        # Класс TestOrdersList: ручка «Список заказов»
│
├── allure_report/                 # Готовый Allure-отчёт 
├── conftest.py                    # Фикстуры: создание курьера и заказов, удаление после теста
├── requirements.txt               # Список библиотек
├── .gitignore                     # Что не отправлять в git (venv, кэш, allure_results)
└── README.md                      # Описание проекта и как его запускать
```

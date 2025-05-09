# Разработка интернет-магазина. 

## Описание:

E-commerce  — электронная торговля, или электронная коммерция.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/a-babushkin/OOP_technology.git
```
2. Установите зависимости:
```
poetry install
```
## Зависимости:

```requires-python = ">=3.11"
dependencies = [
    "python-dotenv (>=1.0.1,<2.0.0)",
    "pandas (>=2.2.3,<3.0.0)",
    "openpyxl (>=3.1.5,<4.0.0)",
    "pandas-stubs (>=2.2.3.241126,<3.0.0.0)"
]

[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.1"
mypy = "^1.14.1"
black = "^24.10.0"
isort = "^5.13.2"


[tool.poetry.group.dev.dependencies]
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

## Настройки Линтеров

```
[tool.black]
line-length = 119
exclude = ".git"

[tool.isort]
line_length = 119

[tool.mypy]
disallow_untyped_defs = true
warn_return_any = true
exclude = 'venv'
```

## Использование:

1. Запускать нужно файл `main.py`

## Тестирование:

- В проекте установлен Pytest фрэймворк и pytest-cov библиотека;
- Прописаны тесты для всех модулей;
- Покрытие тестами проекта равно 100%;
- В папке htmlcov лежит отчет покрытия тестами;

Для самостоятельной проверки покрытия тестами проекта 
запустите в Терминале команду `pytest --cov`
Ддя получения отчета о тестовом покрытии 
запустите в Терминале команду `pytest --cov=src --cov-report=html`

## Добавление новых функций:

- Созданы классы Category и Product
- Для класса Product определены следующие свойства:
    - название (name),
    - описание (description),
    - цена (price),
    - количество в наличии (quantity).
- Для класса Category определены следующие свойства:
    - название (name),
    - описание (description),
    - список товаров категории (products).
- Для этих двух классов добавлена инициализация
- Для класса Category добавлены два атрибута класса:
    - количество категорий
    - количество товаров
- Написаны тесты для классов

## Документация:

Для получения дополнительной информации обратитесь в службу поддержки по телефонам указанным в контактах.

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://opensource.org/license/mit).
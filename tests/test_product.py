from typing import Any
from unittest.mock import patch

from src.product import Product


def test_init(product_fixture: Any) -> None:
    assert product_fixture.name == "Samsung Galaxy C23 Ultra"
    assert product_fixture.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixture.price == 180000.0
    assert product_fixture.quantity == 5


def test_product_create() -> None:
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_new_product() -> None:
    product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter_increase(product_fixture: Any) -> None:
    product_fixture.price = 750000
    assert product_fixture.price == 750000


def test_price_setter_zero(capsys: Any, product_fixture: Any) -> None:
    product_fixture.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_setter_negative(capsys: Any, product_fixture: Any) -> None:
    product_fixture.price = -750
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


@patch("builtins.input", side_effect=["n"])
def test_price_setter_invalid(capsys: Any, product_fixture: Any) -> None:
    product_fixture.price = 800
    assert product_fixture.price, 180000.0

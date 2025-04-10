from typing import Any

import pytest


def test_init(order_fixture1: Any, order_fixture2: Any) -> None:
    assert order_fixture1.order_number == "426/25"
    assert order_fixture1.order_date == "2025-03-09"
    assert order_fixture1.description == "Заказ с базы"

    assert order_fixture1.order_count == 2
    assert order_fixture2.order_count == 2


def test_order_str(order_fixture1: Any) -> None:
    assert str(order_fixture1) == (
        "Заказ №426/25 от 2025-03-09\n      Samsung Galaxy C23 Ultra," " в кол-ве = 5 на сумму 900000.0"
    )


def test_order_product_property(order_fixture1: Any) -> None:
    assert order_fixture1.product == ("Товар - Samsung Galaxy C23 Ultra, в кол-ве = 5 на сумму 900000.0")


def test_order_product_setter(order_fixture1: Any, product_fixture_other: Any) -> None:
    assert order_fixture1.product == "Товар - Samsung Galaxy C23 Ultra, в кол-ве = 5 на сумму 900000.0"
    order_fixture1.product = product_fixture_other
    assert order_fixture1.product == "Товар - Iphone 15, в кол-ве = 8 на сумму 1680000.0"


def test_order_add_product(order_fixture1: Any, product_fixture_other: Any) -> None:
    assert order_fixture1.product == "Товар - Samsung Galaxy C23 Ultra, в кол-ве = 5 на сумму 900000.0"
    order_fixture1.add_product(product_fixture_other)
    assert order_fixture1.product == "Товар - Iphone 15, в кол-ве = 8 на сумму 1680000.0"


def test_order_product_setter_fail(order_fixture1: Any) -> None:
    with pytest.raises(ValueError):
        order_fixture1.product = 1


def test_order_product_setter_smartphone(order_fixture1: Any, product_fixture_smartphone1: Any) -> None:
    order_fixture1.products = product_fixture_smartphone1
    assert order_fixture1.product == "Товар - Samsung Galaxy C23 Ultra, в кол-ве = 5 на сумму 900000.0"


def test_order_products_setter_lawn_grass(order_fixture1: Any, product_fixture_lawn_grass1: Any) -> None:
    order_fixture1.product = product_fixture_lawn_grass1
    assert order_fixture1.product == "Товар - Газонная трава, в кол-ве = 20 на сумму 10000.0"

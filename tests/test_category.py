from typing import Any

import pytest


def test_init(category1_fixture: Any, category2_fixture: Any) -> None:
    assert category1_fixture.name == "Смартфоны"
    assert category1_fixture.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни"
    )
    assert len(category1_fixture.list_of_products) == 2

    assert category1_fixture.category_count == 2
    assert category2_fixture.category_count == 2

    assert category1_fixture.product_count == 3
    assert category2_fixture.product_count == 3


def test_category_str(category1_fixture: Any) -> None:
    assert str(category1_fixture) == "Смартфоны, количество продуктов: 2 шт."


def test_category_products_property(category1_fixture: Any) -> None:
    assert category1_fixture.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_products_setter(category1_fixture: Any, product_fixture: Any) -> None:
    assert len(category1_fixture.list_of_products) == 2
    category1_fixture.products = product_fixture
    assert len(category1_fixture.list_of_products) == 3


def test_category_add_product(category1_fixture: Any, product_fixture: Any) -> None:
    assert category1_fixture.product_count == 12
    category1_fixture.add_product(product_fixture)
    assert category1_fixture.product_count == 13


def test_product_iterator(product_iterator_fixture: Any) -> None:
    iter(product_iterator_fixture)
    assert product_iterator_fixture.index == 0
    assert str(next(product_iterator_fixture)) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(next(product_iterator_fixture)) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."

    with pytest.raises(StopIteration):
        next(product_iterator_fixture)

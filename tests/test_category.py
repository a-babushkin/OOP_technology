from typing import Any

import pytest
from pyexpat.errors import messages

from src.product import Product


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


def test_category_products_setter_fail(category1_fixture: Any) -> None:
    with pytest.raises(ValueError):
        category1_fixture.products = 1


def test_category_products_setter_smartphone(category1_fixture: Any, product_fixture_smartphone1: Any) -> None:
    category1_fixture.products = product_fixture_smartphone1
    assert category1_fixture.list_of_products[-1].name == "Xiaomi Redmi Note 11"


def test_category_products_setter_lawn_grass(category1_fixture: Any, product_fixture_lawn_grass1: Any) -> None:
    category1_fixture.products = product_fixture_lawn_grass1
    assert category1_fixture.list_of_products[-1].name == "Газонная трава"


def test_middle_price(category1_fixture: Any, category_empty_fixture: Any) -> None:
    assert category1_fixture.middle_price() == 195000.0
    assert category_empty_fixture.middle_price() == 0


def test_custom_exception_success(capsys, category1_fixture: Any) -> None:
    assert len(category1_fixture.list_of_products) == 2
    product1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 11)
    category1_fixture.products = product1
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар добавлен успешно"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара в Категорию завершена."
    assert len(category1_fixture.list_of_products) == 3


def test_custom_exception_empty_quantity(capsys, category_empty_fixture: Any) -> None:
    assert len(category_empty_fixture.list_of_products) == 0
    product1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 11)
    product1.quantity = 0
    category_empty_fixture.products = product1
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Укажите правильное кол-во!"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара в Категорию завершена."
    assert len(category_empty_fixture.list_of_products) == 0

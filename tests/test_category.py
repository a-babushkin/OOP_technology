from typing import Any


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


def test_category_products_property(category1_fixture: Any) -> None:
    assert category1_fixture.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_products_setter(category1_fixture: Any, product_fixture: Any) -> None:
    assert len(category1_fixture.list_of_products) == 2
    category1_fixture.products = product_fixture
    assert len(category1_fixture.list_of_products) == 3


def test_category_add_product(category1_fixture: Any, product_fixture: Any) -> None:
    assert category1_fixture.product_count == 10
    category1_fixture.add_product(product_fixture)
    assert category1_fixture.product_count == 11

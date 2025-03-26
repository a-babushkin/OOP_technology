from typing import Any


def test_init(product_fixture: Any) -> None:
    assert product_fixture.name == "Samsung Galaxy C23 Ultra"
    assert product_fixture.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixture.price == 180000.0
    assert product_fixture.quantity == 5

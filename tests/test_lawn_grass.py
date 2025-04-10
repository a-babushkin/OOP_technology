from typing import Any

import pytest


def test_lawn_grass_init(product_fixture_lawn_grass1: Any) -> None:
    assert product_fixture_lawn_grass1.name == "Газонная трава"
    assert product_fixture_lawn_grass1.description == "Элитная трава для газона"
    assert product_fixture_lawn_grass1.price == 500.0
    assert product_fixture_lawn_grass1.quantity == 20
    assert product_fixture_lawn_grass1.country == "Россия"
    assert product_fixture_lawn_grass1.germination_period == "7 дней"
    assert product_fixture_lawn_grass1.color == "Зеленый"


def test_lawn_grass_add(product_fixture_lawn_grass1: Any, product_fixture_lawn_grass2: Any) -> None:
    assert product_fixture_lawn_grass1 + product_fixture_lawn_grass2 == 16750.0


def test_lawn_grass_add_fail(product_fixture_lawn_grass1: Any) -> None:
    with pytest.raises(TypeError):
        print(product_fixture_lawn_grass1 + 1)

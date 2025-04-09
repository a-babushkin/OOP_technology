from typing import Any

import pytest


def test_smartphone_init(product_fixture_smartphone1: Any) -> None:
    assert product_fixture_smartphone1.name == "Xiaomi Redmi Note 11"
    assert product_fixture_smartphone1.description == "1024GB, Синий"
    assert product_fixture_smartphone1.price == 31000.0
    assert product_fixture_smartphone1.quantity == 14
    assert product_fixture_smartphone1.efficiency == 90.3
    assert product_fixture_smartphone1.model == "Note 11"
    assert product_fixture_smartphone1.memory == 1024
    assert product_fixture_smartphone1.color == "Синий"


def test_smartphone_add(product_fixture_smartphone1: Any, product_fixture_smartphone2: Any) -> None:
    assert product_fixture_smartphone1 + product_fixture_smartphone2 == 2114000.0


def test_smartphone_add_fail(product_fixture_smartphone1: Any) -> None:
    with pytest.raises(TypeError):
        print(product_fixture_smartphone1 + 1)

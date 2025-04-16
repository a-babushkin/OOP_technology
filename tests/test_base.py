from typing import Any

from src.base_cat_order import BaseCatOrder
from src.base_product import BaseProduct


class TestCatOrder(BaseCatOrder):
    def __init__(self) -> None:
        self.products = []

    def add_product(self, *args: Any, **kwargs: Any) -> None:
        self.products.append((args, kwargs))


class TestProduct(BaseProduct):
    def __init__(self) -> None:
        self.product = object

    def new_product(self, *args: Any, **kwargs: Any) -> None:
        self.product()


def test_order_add_product_implementation() -> None:
    """Проверяю, что наследник класса Заказы реализует абстрактный метод"""
    order = TestCatOrder()
    assert hasattr(order, "add_product")
    assert callable(order.add_product)


def test_category_add_product_implementation() -> None:
    """Проверяю, что наследник класса Категории реализует абстрактный метод"""
    order = TestProduct()
    assert hasattr(order, "new_product")
    assert callable(order.new_product)

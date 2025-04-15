from tests.conftest import TestCatOrder, TestProduct


def test_order_add_product_implementation():
    """Проверяю, что наследник класса Заказы реализует абстрактный метод"""
    order = TestCatOrder()
    assert hasattr(order, 'add_product')
    assert callable(order.add_product)

def test_category_add_product_implementation():
    """Проверяю, что наследник класса Категории реализует абстрактный метод"""
    order = TestProduct()
    assert hasattr(order, 'new_product')
    assert callable(order.new_product)

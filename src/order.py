from src.base_cat_order import BaseCatOrder
from src.product import Product


class Order(BaseCatOrder):
    order_number: str
    order_date: str
    description: str
    # product: Product

    order_count = 0

    def __init__(self, order_number: str, order_date: str, description: str, product: Product) -> None:
        self.order_number = order_number
        self.order_date = order_date
        self.description = description
        self.__product = product

        Order.order_count += 1

    def add_product(self, product_obj: Product | str) -> None:
        self.__product = product_obj

    def __str__(self) -> str:
        return f"Заказ №{self.order_number} от {self.order_date}\n      {self.__product.name}, в кол-ве = {self.__product.quantity} на сумму {self.__product.quantity * self.__product.price}"

    @property
    def product(self) -> str:
        return f"Товар - {self.__product.name}, в кол-ве = {self.__product.quantity} на сумму {self.__product.quantity * self.__product.price}"

    @product.setter
    def product(self, product_obj: Product) -> None:
        if not isinstance(product_obj, Product):
            raise ValueError("Добавлять можно только объекты класса Product.")
        self.__product = product_obj



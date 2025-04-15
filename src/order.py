from src.base_cat_order import BaseCatOrder
from src.product import Product
from src.exception import ZeroQuantityProduct


class Order(BaseCatOrder):
    order_number: str
    order_date: str
    description: str
    # product: Product

    order_count = 0

    def __init__(self, order_number: str, order_date: str, description: str, product: Product | None) -> None:
        self.order_number = order_number
        self.order_date = order_date
        self.description = description
        self.__product = product

        Order.order_count += 1

    def add_product(self, product_obj: Product | str) -> None:
        self.__product = product_obj

    def __str__(self) -> str:
        return (
            f"Заказ №{self.order_number} от {self.order_date}\n      {self.__product.name}, "
            f"в кол-ве = {self.__product.quantity} на сумму {self.__product.quantity * self.__product.price}"
        )

    @property
    def product(self) -> str:
        return (
            f"Товар - {self.__product.name}, в кол-ве = {self.__product.quantity} "
            f"на сумму {self.__product.quantity * self.__product.price}"
        )

    @product.setter
    def product(self, product_obj: Product) -> None:
        if isinstance(product_obj, Product):
            try:
                if product_obj.quantity < 1:
                    raise ZeroQuantityProduct("Укажите правильное кол-во!")
            except ZeroQuantityProduct as e:
                print(e)
            else:
                self.__product = product_obj
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара в Заказ завершена.")
        else:
            raise ValueError("Добавлять можно только объекты класса Product.")

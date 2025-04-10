from typing import Any

from src.base_product import BaseProduct
from src.output_mixin import OutputMixin


class Product(BaseProduct, OutputMixin):
    name: str
    description: str
    # price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, new_product: dict) -> Any:
        return cls(new_product["name"], new_product["description"], new_product["price"], new_product["quantity"])

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_product_price: float) -> None:
        if new_product_price > 0:
            if self.__price > new_product_price:
                if input("Вы понижаете цену! Продолжить? (y/n)") == "n":
                    print("Цена не изменена.")
                    return
            self.__price = new_product_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

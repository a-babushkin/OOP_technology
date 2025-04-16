from src.base_cat_order import BaseCatOrder
from src.exception import ZeroQuantityProduct
from src.product import Product


class Category(BaseCatOrder):
    name: str
    description: str
    # products: list[object]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[object]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self.list_of_products)} шт."

    def add_product(self, product_obj: Product | str) -> None:
        self.__products.append(product_obj)
        Category.product_count += 1

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @products.setter
    def products(self, product_obj: Product) -> None:
        if isinstance(product_obj, Product):
            try:
                if product_obj.quantity < 1:
                    raise ZeroQuantityProduct("Укажите правильное кол-во!")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product_obj)
                Category.product_count += 1
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара в Категорию завершена.")
        else:
            raise ValueError("Добавлять можно только объекты класса Product.")

    @property
    def list_of_products(self) -> list[object]:
        return self.__products

    def middle_price(self) -> float:
        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0

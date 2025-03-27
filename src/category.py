from src.product import Product


class Category:
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

    def add_product(self, product_obj: Product) -> None:
        self.__products.append(product_obj)
        Category.product_count += 1

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {round(product.price, 2)} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @products.setter
    def products(self, product_obj: Product) -> None:
        self.__products.append(product_obj)
        Category.product_count += 1

    @property
    def list_of_products(self) -> list[object]:
        return self.__products

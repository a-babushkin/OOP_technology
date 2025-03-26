import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json_file(path_to_file: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей."""
    full_path = os.path.abspath(path_to_file)
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def create_object_from_json(file_content: list[dict]) -> list:
    categories = []
    for category in file_content:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


# if __name__ == '__main__':
#     raw_data = read_json_file('../data/products.json')
#     print(raw_data)
#     result = create_object_from_json(raw_data)
#     for item in result:
#         print(item.name)
#         print(item.description)
#
#         for subitem in item.products:
#             print(subitem.name)
#             print(subitem.description)
#             print(subitem.price)
#             print(subitem.quantity)

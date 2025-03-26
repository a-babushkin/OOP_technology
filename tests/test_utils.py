import json
import os
from typing import Any
from unittest.mock import mock_open, patch

from src.category import Category
from src.product import Product
from src.utils import create_object_from_json, read_json_file


@patch("builtins.open")
@patch("json.load")
def test_read_json_file_success(mock_load: Any, mock_open_file: Any) -> None:
    """Тестируем функцию на успешную работу"""
    mock_open_file.new = mock_open()
    mock_load.return_value = [{"name": "Смартфоны"}]

    assert read_json_file("") == [{"name": "Смартфоны"}]


@patch("builtins.open")
@patch("json.load")
def test_read_json_file_json_decode_error(mock_load: Any, mock_open_file: Any) -> None:
    """Тестируем на неверный формат JSON"""
    mock_open_file.new = mock_open()
    mock_load.side_effect = json.JSONDecodeError("Error", "", 1)
    result = read_json_file("")
    assert result == {}


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_open_file: Any) -> None:
    """Тестируем на файл не найден"""
    mock_open_file.new = mock_open()
    result = read_json_file(os.path.abspath("wrong_path.json"))
    assert result == {}
    mock_open_file.assert_called_once_with(os.path.abspath("wrong_path.json"), "r", encoding="utf-8")


def test_create_object_from_json() -> None:
    file_content = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    categories = create_object_from_json(file_content)
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].products[0].price == 180000.0

from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_output_mixin_product(capsys):
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out == 'Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n'


def test_output_mixin_smartphone(capsys):
    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    message = capsys.readouterr()
    assert message.out == 'Smartphone(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)\n'


def test_output_mixin_lawn_grass(capsys):
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out == 'LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)\n'

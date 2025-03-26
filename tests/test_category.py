def test_init(category1_fixture, category2_fixture):
    assert category1_fixture.name == 'Смартфоны'
    assert category1_fixture.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert len(category1_fixture.products) == 2

    assert category1_fixture.category_count == 2
    assert category2_fixture.category_count == 2

    assert category1_fixture.product_count == 3
    assert category2_fixture.product_count == 3

def test_category(
        first_product,
        first_category,
        second_product,
        second_category,
        third_product,
        third_category,
        fourth_product,

):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert first_category.products == [first_product, second_product, third_product]

    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                           "станет вашим другом и помощником")
    assert second_category.products == [first_product, second_product]

    assert third_category.name == "Телевизоры"
    assert third_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                          "станет вашим другом и помощником")
    assert third_category.products == [first_product]

    assert len(first_category.products) == 3
    assert len(second_category.products) == 2
    assert len(third_category.products) == 1

    assert first_category.category_count == 6
    assert second_category.category_count == 6
    assert third_category.category_count == 6

    assert first_category.product_count == 3
    assert second_category.product_count == 3
    assert third_category.product_count == 3

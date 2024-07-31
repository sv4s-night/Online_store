class Product:  # task
    name: str
    description: str    # описание
    price: float
    quantity: str       # количество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity



class Category:     # user
    name: str
    description: str
    products: list

    category_count = 0  # количество категорий
    product_count = 0   # количество товаров


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


        Category.category_count += 1
        Category.product_count += 1

        """
        Атрибуты класса должны заполняться автоматически при инициализации нового объекта.
        Здесь нет необходимости считать количество на складе, можно посчитать длину списка с товарами.
        """


        self.task_list = task_list if task_list else []
        # для вычисления 2х параметров мы обращаемся к классу User и к самой переменной которую надо вычислить (user_count, all_tasks_count)
        User.users_count += 1  # будет увеличиваться на 1 при каждой инициализации экземпляра класса User
        User.all_tasks_count += len(task_list) if task_list else 0






if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, "
                         "но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)


""" Задание 1
Создайте классы Product и Category.

Для класса Product:
название (name), описание (description), цена (price), количество в наличии (quantity).

Для класса Category определите следующие свойства:
название (name), описание (description), список товаров категории (products).


    Подсказка
В задании вам нужно создать два класса, которые вы позже будете развивать. То есть требуется только создать класс
и описать атрибуты, которые будут принадлежать к каждому классу. Хорошая практика — описание типов данных тех значений,
которые будут храниться в атрибутах.

Для каждого поля используйте наиболее подходящий тип данных на ваше усмотрение, но обратите внимание, что цена может
быть указана с копейками, а количество лучше измерять в штуках. Не забывайте, что вы работаете с объектами и классами,
поэтому у класса «Категории» в списке товаров должны храниться именно объекты класса продуктов, то есть в атрибуте
«Список товаров категории» должен быть список объектов класса Product
"""


class Product:
    name: str
    description: str
    price: float
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity



class Category:
    name: str
    description: str
    products: list

    category_count = 0  # количество категорий
    product_count = 0   # количество товаров


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


        self.task_list = task_list if task_list else []
        # для вычисления 2х параметров мы обращаемся к классу User и к самой переменной которую надо вычислить (user_count, all_tasks_count)
        User.users_count += 1  # будет увеличиваться на 1 при каждой инициализации экземпляра класса User
        User.all_tasks_count += len(task_list) if task_list else 0



""" Задание 2
Для этих двух классов, добавьте инициализацию так, чтобы каждый параметр был передан при создании объекта и сохранен.

Также для класса Category добавьте два атрибута класса. Доступ к этим атрибутам должен быть у каждого объекта класса и 
в них должна храниться общая информация для всех объектов. Эти атрибуты хранят в себе количество категорий и количество 
товаров.

Атрибуты класса должны заполняться автоматически при инициализации нового объекта.

Здесь нет необходимости считать количество на складе, можно посчитать длину списка с товарами.
#__init__ #конструктор_класса #self



Подсказка
Важно определить, что принимает на вход метод инициализации, а также какие атрибуты используются через 
self, а какие через Category, чтобы соблюсти доступность сохраненной информации для всех объектов класса Category.

Для автоматического заполнения атрибутов класса Category добавьте в код инициализации увеличение значения 
атрибутов класса на необходимые значения Category.атрибут += значение
"""




""" Задание 3
Напишите тесты для классов, которые проверяют:

корректность инициализации объектов класса Category, корректность инициализации объектов класса Product, 
подсчет количества продуктов, подсчет количества категорий.

#pytest #assert #fixtures


Подсказка
В этом задании важно убедиться, что сделано всё верно, и протестировать реализованный в прошлых пунктах функционал. 
Не переживайте, что можете написать слишком много тестов: лучше проверить, что всё корректно работает и заполняется.
"""



"""* Дополнительное задание
Реализуйте подгрузку данных по категориями и товарам из файл JSON. Для этого опишите специальную функцию, 
которая будет читать файл и создавать объекты классов.

Ссылка на файл: products.json

#json #loads #load

Подсказка
Здесь важно потренировать работу с файлами, а именно JSON-данными. Не забудьте при получении данных из 
файла конвертировать их в объекты.
"""






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

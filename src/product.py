class Product:
    name: str
    description: str
    __price: float
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    """
     Задание 3
Для класса Product необходимо создать класс-метод new_product, который будет принимать на вход параметры товара в
 словаре и возвращать созданный объект класса Product
    
    Подсказка
В класс-методе класса Product необходимо вызывать метод-конструктор __init__ от класса продуктов, 
а созданный объект возвращать как результат работы метода. При этом в класс-метод должны передаваться отдельные 
параметры товара, такие как название, цена, описание и количество на складе.



* Дополнительное задание (к заданию 3)
Для данного метода реализуйте проверку наличия такого же товара схожего по имени. В случае если товар уже существует, 
необходимо сложить количество в наличии старого товара и нового. При конфликте цен выбрать ту, которая является более 
высокой. Для этого можно в метод передать список товаров, в котором нужно искать дубликаты.

Подсказка
Речь идет о работе со списком товаров, которые уже были добавлены. Не бойтесь передавать новые атрибуты в класс-методы, 
которые создаете. Проверка товара заключается в переборе имеющегося списка товаров и сравнения названий.
    """

    @classmethod
    def new_product(cls, product_dict):
        existing_products = []

        for product in existing_products:
            if product.name == product_dict['name']:
                product.quantity += product_dict['quantity']
                product.price = max(product.price, product_dict['price'])
                return product

        new_product = cls(product_dict['name'], product_dict['description'], product_dict['price'],
                          product_dict['quantity'])
        existing_products.append(new_product)
        return new_product


    """ Задание 4
    Для класса Product сделайте атрибут цены приватным и опишите геттеры и сеттеры. В сеттере реализуйте проверку: 
    в случае если цена равна или ниже нуля, выводите сообщение в консоль “Цена не должна быть нулевая или отрицательная”, 
    при этом новую цену устанавливать не нужно.
    
    
    Подсказка
    Задание посвящено работе с геттерами и сеттерами. Мы защищаем пользователя от случайного введения некорректной цены. 
    То есть необходимо выводить сообщение, только если цена ниже или равна нулю, чтобы не продать товар бесплатно.
    
    
    
    * Дополнительное задание (к заданию 4)
    В случае если цена товара понижается, добавить логику подтверждения пользователем вручную через ввод y (значит yes) 
    или n (значит no) для согласия понизить цену или для отмены действия соответственно.
    
    Проще всего в сеттере вывести сообщение через input и обработать ответ, где y считается за согласие, 
    а любой другой ответ отменяет действие.
    
    
    Подсказка
Расширяем прошлую задачу и предоставляем пользователю большую защиту от введения некорректной цены. Обратите внимание, 
что логика защиты срабатывает, когда цена просто ниже прошлой.
    """



    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
        else:
            confirmation = input("Вы подтверждаете изменение цены? (y/n): ")
            if confirmation.lower() == 'y':
                self.__price = new_price
                print("Цена успешно обновлена.")
            else:
                print("Изменение цены отменено.")



    """ Задание 5
Напишите тесты для нового функционала. При этом убедитесь что тесты, которые были написаны ранее выполняются без ошибок.
    
    """


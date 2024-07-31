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

import json
from src.product import Product
from src.category import Category



def data_json(path: str) -> list[dict:dict]:
    """Функция принимает путь до json файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def create_object(data):
    """Функция создающая объект класса"""
    prod = []
    for i in data:
        desc = []
        for j in i["products"]:
            desc.append(Product(**j))
        i["products"] = desc
        prod.append(Category(**i))
    return prod

import json

from django.core.management import BaseCommand
from django.db import connection

from cars.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        categories = []
        # Здесь мы получаем данные из фикстурв с категориями
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "cars.category":
                    categories.append(item)
        return categories

    @staticmethod
    def json_read_products():
        products = []
        # Здесь мы получаем данные из фикстурв с продуктами
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "cars.product":
                    products.append(item['fields'])
        return products

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE cars_category RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE cars_product RESTART IDENTITY CASCADE;")
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(Category(
                pk=category['pk'],
                name=category['fields']['name'],
                description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(Product(
                name=product['name'],

                description=product['description'],
                photo=product['photo'],
                category=Category.objects.get(pk=product['category']),
                price=product['price']))

        # print(product_for_create)

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

import csv

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Импорт ингредиентов из csv файла'

    def handle(self, *args, **kwargs):
        with open(
            'recipes/data/ingredients.csv', 'r', encoding='utf-8'
        ) as file:
            reader = csv.DictReader(file)
            Ingredient.objects.bulk_create(
                Ingredient(**row) for row in reader
            )
        self.stdout.write(self.style.SUCCESS('Ингредиенты загружены'))
        return 'OK'

import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for tel in phones:
            phone = Phone(
                name=tel['name'],
                image=tel['image'],
                price=tel['price'],
                release_date=tel['release_date'],
                lte_exists=tel['lte_exists'],
                slug=slugify(tel['name'])
            )
            phone.save()
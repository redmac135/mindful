from django.core.management.base import BaseCommand
from ...models import QuoteResponse
import csv

class Command(BaseCommand):
    help = 'Creates QuoteResponse Objects based on csv file'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--delete', action='store_true', help='Indicates to clear existing quotes')

    def handle(self, *args, **kwargs):
        delete = kwargs['delete']

        f = open('reflection/fixtures/quoteresponses.csv')
        csv_reader = csv.reader(f)
        data_list = list(csv_reader)

        for line in data_list[1:]:
            QuoteResponse.objects.create(
                quote = line[0],
                author = line[1],
                happysad = line[2],
            )

        if delete:
            QuoteResponse.objects.all().delete()
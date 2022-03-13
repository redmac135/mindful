from django.core.management.base import BaseCommand
from ...models import AdjectiveChoice
from ...choices import ADJECTIVE_CHOICES_1, ADJECTIVE_CHOICES_2, ADJECTIVE_CHOICES_3, ADJECTIVE_CHOICES_4, ADJECTIVE_CHOICES_5

class Command(BaseCommand):
    help = 'Creates AdjectiveChoice Objects based on choices.py'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--delete', action='store_true', help='Indicates to clear existing choices')

    def handle(self, *args, **kwargs):
        delete = kwargs['delete']
        choicelists = [ADJECTIVE_CHOICES_1, ADJECTIVE_CHOICES_2, ADJECTIVE_CHOICES_3, ADJECTIVE_CHOICES_4, ADJECTIVE_CHOICES_5]
        counter = 1

        if delete:
            AdjectiveChoice.objects.all().delete()

        for choicelist in choicelists:
            for (id, adjective) in choicelist:
                AdjectiveChoice.objects.create(
                    feeling=counter,
                    order=id,
                    adjective=adjective,
                )
            counter += 1
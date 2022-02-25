from django.core.management.base import BaseCommand
from ...models import RegistrationToken

class Command(BaseCommand):
    help = 'Creates or Deletes Admin series Registration Tokens'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--delete', action='store_true', help='Indicates to delete all admin token objects')
        parser.add_argument('-c', '--create', action='store_true', help='Indicates to create 10 admin token objects')

    def handle(self, *args, **kwargs):
        delete = kwargs['delete']
        create = kwargs['create']

        if delete:
            RegistrationToken.objects.filter(token__icontains='ADMIN').delete()
        
        if create:
            for i in range(10):
                RegistrationToken.objects.create(
                    token='ADMIN' + str(i),
                    valid=True
                )

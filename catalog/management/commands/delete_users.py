from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('users', nargs='*', type=int, choices=range(1, 11))

    def handle(self, *args, **options):

        for i in options["users"]:
            b = User.objects.get(pk=int(i))
            User.objects.filter(username=b).delete()




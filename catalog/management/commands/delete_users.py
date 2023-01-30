from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('users', nargs='*', type=int)

    def handle(self, *args, **options):
        d = User.objects.filter(id__in=options["users"])
        d.delete()




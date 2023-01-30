from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('users', type=int, choices=range(1, 11))

    def handle(self, *args, **options):

        for i in range(1, options["users"]+1):
            p = User.objects.create(username=Faker().name(), email=Faker().email(), password=Faker().password())
            p.save()




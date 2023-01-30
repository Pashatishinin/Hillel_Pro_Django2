from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('users', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        User.objects.bulk_create([User(username=Faker().email().split('@')[0],
                                       email=Faker().email(),
                                       password=Faker().password()) for _ in range(options["users"])])









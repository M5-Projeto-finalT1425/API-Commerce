from accounts.models import Account
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin user"

    def add_arguments(self, parser):
        ...
        parser.add_argument(
            "-u",
            "--username",
            type=str,
            help="Define the admin username",
        ),

        parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="Define the admin password",
        ),

        parser.add_argument(
            "-e",
            "--email",
            type=str,
            help="Define the admin email",
        )

    def handle(self, *args: tuple, **kwargs: dict):
        username = kwargs["username"]
        password = kwargs["password"]
        email = kwargs["email"]

        if not username:
            username = "admin"
        if not password:
            password = "admin1234"
        if not email:
            email = f"{username}@example.com"

        try:
            Account.objects.get(username__exact=username)
            raise CommandError(f"Username `{username}` already taken.")
        except Account.DoesNotExist:
            pass

        try:
            Account.objects.get(email__exact=email)
            raise CommandError(f"Email `{email}` already taken.")
        except Account.DoesNotExist:
            pass

        Account.objects.create_superuser(
            username=username, email=email, password=password
        )
        self.stdout.write(
            self.style.SUCCESS(f"Admin `{username}` successfully created!")
        )

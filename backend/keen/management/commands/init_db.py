from django.core.management.base import BaseCommand

from utils.seed_database import DatabaseSeeder


class Command(BaseCommand):
    help = "Generates dummy data for a dev environment."

    def handle(self, *args, **kwargs):

        dbs = DatabaseSeeder()

        # dbs.wipe_database()
        dbs.populate()

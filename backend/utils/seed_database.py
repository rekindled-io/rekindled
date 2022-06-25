import random
from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError
from django.utils.text import slugify

from games.models import Game, GameAndPlatform, Platform
from handles.models import Handle
from kindles.models import DirectKindle, SeekingKindle
from rekindled import settings

from .testing_factories import (GameAndPlatformFactory, GameFactory,
                                GameWithPlatformFactory, HandleFactory,
                                PlatformFactory, UserFactory)

User = get_user_model()


class DatabaseSeeder:
    """
    Quick and dirty way to preseed the database with randomised data for testing/development work.
    """

    MODELS = [User, Handle, SeekingKindle, DirectKindle, Game, Platform]

    GAME_CHOICES = [
        "Minecraft",
        "Final Fantasy",
        "Diablo",
        "Fortnite",
        "World of Warcraft",
        "Overwatch",
        "Destiny",
        "Halo",
        "Call of Duty",
        "Battlefield",
        "Dota",
        "League of Legends",
    ]

    PLATFORM_CHOICES = [
        "PC",
        "Playstation Network",
        "Nintendo Network",
        "Xbox Network",
        "Steam",
    ]

    def __init__(
        self,
        num_users=1,
        num_platforms=0,
        num_games=0,
        num_handles=1,
        delete_data=False,
    ):
        if num_platforms == 0:
            num_platforms = len(DatabaseSeeder.PLATFORM_CHOICES)

        if num_games == 0:
            num_games = len(DatabaseSeeder.GAME_CHOICES)

        self.num_users = num_users
        self.num_platforms = num_platforms
        self.num_games = num_games
        self.num_handles = 1

        self.users = []
        self.games = []
        self.platforms = []
        self.gamesandplatforms = []
        self.handles = []

        self.delete_data = delete_data

    def wipe_database(self):
        """
        This will wipe absolutely everything in the DB. Only to be used in non-production.
        """
        if self.delete_data and settings.DEBUG:
            for model in models:
                model.objects.all().delete()

    def populate(self):
        """
        Note that the sequence is important (User -> Platform -> Game -> Handle) due to the interdependencies.
        """
        random.seed(datetime.now())

        for _ in range(self.num_users):
            print(f"Populating database with {self.num_users} user/s...")
            UserFactory()

        self.users = list(User.objects.all())

        for name in DatabaseSeeder.PLATFORM_CHOICES[: self.num_platforms]:
            try:
                PlatformFactory(name=name)
            except IntegrityError:
                print(f"Platform {name} already exists, skipping.")
                pass

        self.platforms = list(Platform.objects.all())

        for name in DatabaseSeeder.GAME_CHOICES[: self.num_games]:
            platform = random.choices(self.platforms)

            try:
                GameWithPlatformFactory.create(
                    name=name, slug=slugify(name), platforms=platform
                )
            except IntegrityError:
                print(f"{name}/{platform[0]} combination already exists, skipping.")
                pass

        self.games = list(GameAndPlatform.objects.all())

        if self.num_users != 0:
            for game in self.games:
                user = random.choice(self.users)
                region = random.choice(Handle._meta.get_field("region").choices)

                for _ in range(random.randint(1, self.num_handles)):
                    handle = HandleFactory(
                        user=user, game_and_platform=game, region=region[0]
                    )
                    self.handles.append(handle)

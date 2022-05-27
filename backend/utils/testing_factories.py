import datetime
import random

import factory
import faker
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from games.models import Game, GameAndPlatform, Platform
from handles.models import Handle

User = get_user_model()

fake = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.LazyFunction(lambda: make_password("pi3.1415"))
    email = factory.Faker("email")


class PlatformFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Platform

    name = factory.LazyAttribute(lambda o: f"{o}")


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Faker(lambda o: f"{o}")
    slug = factory.LazyAttribute(lambda o: f"{o}")


class GameAndPlatformFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GameAndPlatform

    platform = factory.SubFactory(PlatformFactory)


class GameWithPlatformFactory(GameFactory):
    @factory.post_generation
    def platforms(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for platform in extracted:
                self.platforms.add(platform)


class HandleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Handle

    name = factory.LazyAttribute(
        lambda _: f"{fake.user_name()}{random.randint(100, 10000)}"
    )
    gameandplatform = factory.SubFactory(GameAndPlatformFactory)
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def gameandplatform(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for gameandplatform in extracted:
                self.gameandplatform.add(gameandplatform)

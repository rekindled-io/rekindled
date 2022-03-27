import factory
import faker
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

fake = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.LazyFunction(lambda: make_password("pi3.1415"))
    email = factory.Faker("email")

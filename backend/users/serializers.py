import requests

from django.contrib.auth import get_user_model
from rest_framework import fields, serializers
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator
from rekindled import settings

import hashlib

from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "bio",
            "location",
            "discord_name",
            "discord_account_number",
            "discord_id",
            "steam_id",
        ]


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    profile = ProfileSerializer(partial=True, required=False)
    password_confirm = fields.CharField(write_only=True)
    original_email = serializers.SerializerMethodField()
    hashed_email = serializers.SerializerMethodField()
    captcha = serializers.CharField(write_only=True)

    class Meta:
        model = User
        related_fields = ["profile"]
        fields = [
            "username",
            "password",
            "password_confirm",
            "is_active",
            "last_login",
            "date_joined",
            "email",
            "profile",
            "original_email",
            "hashed_email",
            "captcha",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "last_login": {"read_only": True},
            "date_joined": {"read_only": True},
            "is_active": {"read_only": True},
        }

    def validate(self, data):
        if self.context["request"].method == "POST":
            if data["password"] != data["password_confirm"]:
                raise ValidationError({"password_confirm": "Passwords do not match."})
        return data

    def create(self, validated_data):
        if "password_confirm" in validated_data:
            del validated_data["password_confirm"]
        if "profile" in validated_data:
            del validated_data["profile"]
        if "captcha" in validated_data:
            del validated_data["captcha"]

        user = get_user_model().objects.create_user(**validated_data)

        return user

    def update(self, instance, validated_data):
        for related_obj_name in self.Meta.related_fields:
            try:
                data = validated_data.pop(related_obj_name)
                related_instance = getattr(instance, related_obj_name)

                for attr_name, value in data.items():
                    setattr(related_instance, attr_name, value)
                related_instance.save()
            except KeyError:
                pass
        return super().update(instance, validated_data)

    def get_original_email(self, obj):
        """
        Only show unhashed email if it's the owner for privacy reasons.
        """
        if request := self.context.get("request"):
            if not request.user == obj:
                return ""
        return obj.email

    def get_hashed_email(self, obj):
        """
        Hashed email is required for Gravatar to work.
        """
        hashed = obj.email.encode()
        return hashlib.md5(hashed).hexdigest()

    def validate_captcha(self, value):
        SECRET_KEY = settings.CAPTCHA_SECRET_KEY

        if settings.DEBUG:
            # These are dummy values used for testing, reference -
            # https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do
            value = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"

        try:
            url = f"https://www.google.com/recaptcha/api/siteverify?secret={SECRET_KEY}&response={value}"
            res = requests.get(url, headers={"Content-Type": "application/json"})
            if not res.json()["success"]:
                raise ValidationError({"detail": "Invalid captcha token."})
        except requests.HTTPError:
            raise ValidationError({"detail": "Error validating CAPTCHA."})

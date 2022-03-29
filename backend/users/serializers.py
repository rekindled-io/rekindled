from django.contrib.auth import get_user_model
from rest_framework import fields, serializers
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator

from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["bio", "location"]


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    profile = ProfileSerializer(partial=True, required=False)
    password_confirm = fields.CharField(write_only=True)
    original_email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password_confirm",
            "is_active",
            "last_login",
            "date_joined",
            "email",
            "profile",
            "original_email"
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

        user = get_user_model().objects.create_user(**validated_data)

        return user

    def get_original_email(self, obj):
        """
        Only show unhashed email if it's the owner for privacy reasons.
        """
        if request := self.context.get("request"):
            if not request.user == obj:
                return ""
        return obj.email

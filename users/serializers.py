from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "phone", "job", "age", "type")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "phone", "job", "age", "type")
        read_only_fields = ("id",)


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "age",
            "username",
            "job",
            "type",
            "address",
            "email",
            "phone",
            "password1",
            "password2"
        )
        read_only_fields = ("id",)

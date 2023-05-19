from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainSerializer, PasswordField
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "phone", "job", "age", "type")


class CustomTokenObtainPairSerializer(serializers.Serializer):
    token_class = RefreshToken

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"] = serializers.CharField(required=False)
        self.fields["username"] = serializers.CharField(required=False)
        self.fields["password"] = PasswordField()

    default_error_messages = {
        "no_active_account": _("No active account found with the given credentials")
    }

    def validate(self, attrs):
        data = super().validate(attrs)
        email = attrs.get("email")
        username = attrs.get("username")
        if email and username:
            raise ValidationError("Please send email or username.")
        authenticate_kwargs = {
            "email": attrs.get("email"),
            "username": attrs.get("username"),
            "password": attrs.get("password"),
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        print(authenticate_kwargs)

        user = authenticate(**authenticate_kwargs)

        # if not api_settings.USER_AUTHENTICATION_RULE(user):
        #     raise exceptions.AuthenticationFailed(
        #         self.error_messages["no_active_account"],
        #         "no_active_account",
        #     )

        refresh = self.get_token(user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = UserSerializer(user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return data

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)


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
            "email",
            "password1",
            "password2"
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.pop("password2", None)
        username = attrs.get("username")
        user = User.objects.filter(username=username).exists() if username else None
        if user:
            raise ValidationError(_('Username is already taken.'))
        if password2 != password1:
            raise ValidationError(_("Passwords didn't match."))
        return super().validate(attrs)

    def create(self, validated_data):
        password1 = validated_data.pop("password1", None)
        user = User(**validated_data)
        user.set_password(password1)
        user.save()
        return user

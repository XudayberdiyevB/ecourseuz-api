from rest_framework import serializers

from . import google, facebook
from .register import register_social_user


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)
        try:
            email = user_data['email']
            name = user_data['name']
            return register_social_user(email=email, name=name)
        except Exception as identifier:
            raise serializers.ValidationError('The token  is invalid or expired. Please login again.')


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:  # noqa
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        # if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
        #     raise AuthenticationFailed('oops, who are you?')

        email = user_data['email']
        name = user_data['name']
        first_name = user_data['given_name']
        last_name = user_data['family_name']

        return register_social_user(email=email, name=name, first_name=first_name, last_name=last_name)

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token


class UserRegistrationSerializers(serializers.ModelSerializer):
    # User registration  api data formatter.
    class Meta:  # pylint: disable=too-few-public-methods
        # Return default User options fields.
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    # pylint: disable=R0201
    def create(self, validated_data):  # create User && Profile profile model.
        profile_data = validated_data
        user = User.objects.create_user(**profile_data)
        Token.objects.create(user=user)
        return user

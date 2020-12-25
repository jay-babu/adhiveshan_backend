from typing import Dict

from rest_framework import serializers

from . import constants
from . import models
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True, required=True,
                                     style={'input_type': 'password'})
    email = serializers.EmailField(max_length=255, min_length=4, required=True)
    first_name = serializers.CharField(max_length=255, min_length=2, required=True)
    last_name = serializers.CharField(max_length=255, min_length=2, required=True)
    center = serializers.ChoiceField(
        choices=sorted(list(map(lambda item: item.replace('_', ' ').title(), constants.CENTERS_REGIONS.keys()))),
        required=True)
    gender = serializers.ChoiceField(choices=list(map(lambda item: item.replace('_', ' ').title(), constants.GENDERS)),
                                     required=True)
    mandal = serializers.ChoiceField(choices=list(map(lambda item: item.replace('_', ' ').title(), constants.MANDALS)),
                                     required=True)

    class Meta:
        model = models.User
        fields = ('email', 'first_name', 'last_name', 'center', 'gender', 'mandal', 'password',)

    def validate(self, attrs: Dict[str, str]):
        if not (center := attrs.get('center', None)):
            raise serializers.ValidationError(f'Please select a Center')

        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(f'An user with email: {email} already exists in the database')

        attrs['region']: str = constants.CENTERS_REGIONS.get(center.lower().replace(' ', '_'), '')
        return super().validate(attrs)

    def create(self, validated_data: Dict[str, str]):
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    model = models.User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(max_length=65, min_length=8, write_only=True, required=True,
                                         style={'input_type': 'password'})
    new_password = serializers.CharField(max_length=65, min_length=8, write_only=True, required=True,
                                         style={'input_type': 'password'})

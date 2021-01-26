import functools
from typing import Dict

from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError as DVE

from adhiveshan_backend import settings
from . import constants
from . import models
from .models import User, title_and_capitial, ExternalUserModel


@functools.lru_cache(maxsize=None)
def get_default_password_validators():
    return get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)


def get_password_validators(validator_config):
    validators = []
    for validator in validator_config:
        try:
            klass = import_string(validator['NAME'])
        except ImportError:
            msg = "The module in NAME could not be imported: %s. Check your AUTH_PASSWORD_VALIDATORS setting."
            raise ImproperlyConfigured(msg % validator['NAME'])
        validators.append(klass(**validator.get('OPTIONS', {})))

    return validators


def validate_password(password, user=None, password_validators=None):
    """
    Validate whether the password meets all validator requirements.

    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError with all error messages.
    """
    if password_validators is None:
        password_validators = get_default_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, user)
        except DVE as error:
            raise ValidationError({'new_password': error.message})


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True, required=True,
                                     style={'input_type': 'password'})
    email = serializers.EmailField(max_length=255, min_length=4, required=True)
    first_name = serializers.CharField(max_length=60, min_length=2, required=True)
    middle_name = serializers.CharField(max_length=60, min_length=1, required=False)
    last_name = serializers.CharField(max_length=60, min_length=2, required=True)
    center = serializers.ChoiceField(
        choices=sorted(map(lambda center: center.replace('_', ' ').title()
        if len(center.split('_')) == 1
        else title_and_capitial(center.replace('_', ' ')), constants.CENTERS_REGIONS.keys()))
    )
    gender = serializers.ChoiceField(
        choices=sorted(map(lambda item: item.replace('_', ' ').title(), constants.GENDERS), reverse=True),
        required=True)
    mandal = serializers.ChoiceField(
        choices=sorted(map(lambda item: item.replace('_', ' ').title(), constants.MANDALS)),
        required=True)

    class Meta:
        model = models.User
        fields = ('email', 'first_name', 'last_name', 'center', 'gender', 'mandal', 'password', 'middle_name',)

    def validate(self, attrs: Dict[str, str]):
        if not (center := attrs.get('center', None)):
            raise serializers.ValidationError(f'Please select a Center')

        user = self.context.user
        validate_password(attrs.get('password', ''), user)

        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(f'An user with email: {email} already exists in the database')

        attrs['region']: str = constants.CENTERS_REGIONS.get(center.lower().replace(' ', '_'), '')
        return super().validate(attrs)

    def create(self, validated_data: Dict[str, str]):
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(max_length=65, min_length=8, required=True,
                                         style={'input_type': 'password'})
    new_password = serializers.CharField(max_length=65, min_length=8, required=True,
                                         style={'input_type': 'password'})

    def validate(self, attrs):
        user = self.context.user
        if not user.check_password(attrs.get('old_password')):
            raise ValidationError({"old_password": ["Wrong password."]})
        validate_password(attrs.get('new_password', ''), user)
        return super().validate(attrs)


class CreateExternalTokenSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(required=False, min_value=99999, )
    code_expiration = serializers.DateTimeField(required=False, write_only=True)
    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())

    class Meta:
        model = ExternalUserModel
        fields = ('user', 'code', 'code_expiration',)

    def create(self, validated_data):
        user = validated_data.pop('user', None)
        obj, _ = ExternalUserModel.objects.update_or_create(user=user, defaults=validated_data)
        return obj

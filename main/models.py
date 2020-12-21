from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from . import constants


class UserManager(BaseUserManager):
    """Manager for the User class."""
    def create_user(self,
                    email: str,
                    password: str,
                    first_name: str = None,
                    last_name: str = None) -> 'User':
        """Create a user."""
        if not email or not password:
            raise Exception

        if User.objects.filter(email=email).exists():
            raise Exception('An user with email: {} already exists in the database')

        normalized_email: str = self.normalize_email(email=email)
        user: User = self.model(email=normalized_email)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str) -> 'User':
        """Create a superuser. Superusers can log into the admin platform."""
        superuser: User = self.create_user(email=email, password=password)
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser

    def create_user_from_json(self, data) -> 'User':
        """Creates a user from a JSON payload.
        Args:
            data: A dict like object containing data to instantiate a user with.
        Raises:
            DataForNewUserNotProvidedException: If required data are not
                provided.
        Returns:
            The created User object.
        """
        try:
            email = data['email']
            password = data['password']
            first_name = data['first_name']
            last_name = data['last_name']
        except KeyError:
            raise Exception

        user = User.objects.create_user(email=email,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name)
        return user


class User(AbstractBaseUser):
    """The Base User main."""
    email: models.EmailField = models.EmailField(max_length=60, unique=True)
    date_joined: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    is_active: models.BooleanField = models.BooleanField(default=True)
    is_admin: models.BooleanField = models.BooleanField(default=False)
    is_superuser: models.BooleanField = models.BooleanField(default=False)
    first_name: models.CharField = models.CharField(max_length=60)
    last_name: models.CharField = models.CharField(max_length=60)
    region = models.CharField(max_length=60, choices=constants.REGIONS, null=True)
    center = models.CharField(max_length=60, choices=constants.CENTERS, null=True)
    side = models.CharField(max_length=60, choices=constants.SIDES, null=True)
    mandal = models.CharField(max_length=60, choices=constants.MANDALS, null=True)

    objects: UserManager = UserManager()

    # Specify which field the user will log in with.
    USERNAME_FIELD: str = 'email'
    EMAIL_FIELD: str = 'email'

    def __str__(self) -> str:
        return str(self.email.__str__())

    def full_name(self) -> str:
        return self.first_name + ' ' + self.last_name

    def is_staff(self) -> models.BooleanField:
        return self.is_admin

    def has_perm(self, perm: str, obj=None) -> models.BooleanField:
        return self.is_admin

    def has_module_perms(self, app_label: str) -> models.BooleanField:
        return self.is_admin


class Pledge(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pledge',
        null=True)

    def __str__(self):
        return self.user.email


class Module(models.Model):
    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE, related_name='modules')
    type = models.CharField(max_length=60, choices=constants.MODULE_TYPES, null=True)
    tier = models.CharField(max_length=60, choices=constants.TIERS, null=True)
    is_selectable = models.BooleanField(default=True)

    def __str__(self):
        return self.type + ', ' + self.tier + ', for ' + self.pledge.user.email


class MukhpathItem(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60, choices=constants.MODULE_TYPES)
    english_content = models.CharField(max_length=60)
    gujurati_content = models.CharField(max_length=60)
    transliteration_content = models.CharField(max_length=60)
    audio_url = models.CharField(max_length=60)
    video_url = models.CharField(max_length=60)

    def __str__(self):
        return self.name + ', ' + self.type


class MukhpathItemInstance(models.Model):
    mukhpath_item = models.ForeignKey(MukhpathItem, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    is_memorized = models.BooleanField(default=False)

    def __str__(self):
        return self.mukhpath_item.name + ', ' + self.mukhpath_item.type + ', for ' + self.module.pledge.user.email

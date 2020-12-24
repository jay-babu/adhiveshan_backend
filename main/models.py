from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models

from . import constants


class UserManager(BaseUserManager):
    """Manager for the User class."""

    def create_user(self,
                    email: str,
                    password: str,
                    first_name: str = '',
                    last_name: str = '',
                    region: str = '',
                    center: str = '',
                    gender: str = '',
                    mandal: str = '', ) -> 'User':
        """Create a user."""
        if not email:
            raise ValidationError(f'Please provide an email')
        if not password:
            raise ValidationError(f'Please provide a password')

        if User.objects.filter(email=email).exists():
            raise ValidationError(f'An user with email: {email} already exists in the database')

        normalized_email: str = self.normalize_email(email=email)
        user: User = self.model(email=normalized_email)
        user.first_name = first_name
        user.last_name = last_name
        user.region = region
        user.center = center
        user.gender = gender
        user.mandal = mandal

        return user

    def create_superuser(self, email: str, password: str) -> 'User':
        """Create a superuser. Superusers can log into the admin platform."""
        superuser: User = self.model(email=email)
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser):
    """The Base User main."""
    email: models.EmailField = models.EmailField(max_length=60, unique=True)
    date_joined: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    is_active: models.BooleanField = models.BooleanField(default=True)
    is_admin: models.BooleanField = models.BooleanField(default=False)
    is_superuser: models.BooleanField = models.BooleanField(default=False)
    first_name: models.CharField = models.CharField(max_length=60, null=True)
    last_name: models.CharField = models.CharField(max_length=60, null=True)
    region = models.CharField(max_length=60,
                              choices=[(region, region.replace('_', ' ').title()) for region in constants.REGIONS],
                              null=True)
    center = models.CharField(max_length=60,
                              choices=[(center, center.replace('_', ' ').title()) for center in
                                       constants.CENTERS_REGIONS.keys()],
                              null=True)
    gender = models.CharField(max_length=60,
                              choices=[(gender, gender.replace('_', ' ').title()) for gender in constants.GENDERS],
                              null=True)
    mandal = models.CharField(max_length=60,
                              choices=[(mandal, mandal.replace('_', ' ').title()) for mandal in constants.MANDALS],
                              null=True)

    objects: UserManager = UserManager()

    # Specify which field the user will log in with.
    USERNAME_FIELD: str = 'email'
    EMAIL_FIELD: str = 'email'

    def __str__(self) -> str:
        return f'{self.email}'

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def is_staff(self) -> models.BooleanField:
        return self.is_admin

    def has_perm(self, perm: str, obj=None) -> models.BooleanField:
        return self.is_admin

    def has_module_perms(self, app_label: str) -> models.BooleanField:
        return self.is_admin


class Module(models.Model):
    title = models.CharField(max_length=60, null=True)
    imageURL = models.URLField(null=True)
    is_selectable = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ModuleInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.module.title}, for {self.user.email}'


class Pledge(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        return self.user.email


class PledgedModule(models.Model):
    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    tier = models.CharField(max_length=60, choices=constants.TIERS, null=True)

    def __str__(self):
        return f'{self.module.title} pledged for {self.tier} tier'


class MukhpathItem(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    english_content = models.CharField(max_length=60)
    gujurati_content = models.CharField(max_length=60)
    transliteration_content = models.CharField(max_length=60)
    audio_url = models.CharField(max_length=60)
    video_url = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.name}, {self.module.title}'


class MukhpathItemInstance(models.Model):
    mukhpath_item = models.ForeignKey(MukhpathItem, on_delete=models.CASCADE)
    module_instance = models.ForeignKey(ModuleInstance, on_delete=models.CASCADE, null=True)
    is_memorized = models.BooleanField(default=False)
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.mukhpath_item.name}, {self.module_instance.module.title}, for {self.module_instance.user.email}'

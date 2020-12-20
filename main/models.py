from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Manager for the User class."""
    def create_user(self, email: str, password: str, first_name: str, last_name: str) -> 'User':
        """Create a user."""
        if not email or not password or not not first_name or not last_name:
            raise Exception

        if User.objects.filter(email=email).exists():
            raise Exception('An user with email: {} already exists in the database')

        normalized_email: str = self.normalize_email(email=email)
        user: User = self.model(email=normalized_email)
        user.first_name = first_name
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


class User(AbstractBaseUser):
    """The Base User main."""
    email: models.EmailField = models.EmailField(max_length=60, unique=True)
    date_joined: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    is_active: models.BooleanField = models.BooleanField(default=True)
    is_admin: models.BooleanField = models.BooleanField(default=False)
    is_superuser: models.BooleanField = models.BooleanField(default=False)
    first_name: models.CharField = models.CharField(max_length=60)
    last_name: models.CharField = models.CharField(max_length=60)

    objects: UserManager = UserManager()

    # Specify which field the user will log in with.
    USERNAME_FIELD: str = 'email'
    EMAIL_FIELD: str = 'email'

    def __str__(self) -> str:
        return str(self.email.__str__())

    def is_staff(self) -> models.BooleanField:
        return self.is_admin

    def has_perm(self, perm: str, obj=None) -> models.BooleanField:
        return self.is_admin

    def has_module_perms(self, app_label: str) -> models.BooleanField:
        return self.is_admin

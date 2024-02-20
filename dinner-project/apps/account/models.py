from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Tripmate Custom User Manager"""

    use_in_migrations = True

    def create_superuser(self, email, password, **extra_fields):
        """Creates and saves a superuser."""

        user = self.model(**extra_fields)
        user.email = email
        user.password = make_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)

    # 기본 정보
    is_staff = models.BooleanField(
        default=False,
        help_text=_("관리자인지 확인"),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_("활성화 된 유저인지 확인"),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

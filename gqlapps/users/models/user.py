from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ..managers.user import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('e-mail'),
        unique=True
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=20,
    )
    slug = models.SlugField(blank=True)
    is_active = models.BooleanField(
        verbose_name=_('active status'),
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('Is staff'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Is superuser'),
        default=False
    )
    firstname = models.CharField(
        verbose_name=_('First name'),
        max_length=50, blank=True
    )
    lastname = models.CharField(
        verbose_name=_('Last name'),
        max_length=50, blank=True
    )
    dob = models.DateField(
        verbose_name=_('Date of Birth'),
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def display_age(self):
        if self.dob:
            now = timezone.now()
            years = now - self.dob


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    mobile_phone_regex = RegexValidator(regex=r'^09|^\+\d+$',
                                   message="Please enter a valid phone number")
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='ایمیل')
    username = models.CharField(max_length=13, unique=True, null=False, verbose_name='شماره موبایل\نام کاربری')
    first_name = models.CharField(max_length=128, verbose_name='نام')
    last_name = models.CharField(max_length=128, verbose_name='نام خانوادگی')
    USERNAME_FIELD = 'username'

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_permissions_set',
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
        related_query_name='user',
    )

    def __str__(self) -> str:
        return self.username

    def get_username(self):
        return self.username
    
    class Meta:
        verbose_name = 'کاربر'
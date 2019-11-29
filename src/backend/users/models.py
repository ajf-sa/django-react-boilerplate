from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, phone, passwrod=None):
        if not phone.isdigit():
            raise TypeError('Phone must be a Digit.')

        phone_len = getattr(settings, 'PHONE_LEN', 9)
        if len(phone) < phone_len:
            raise TypeError('Phone length must be bigger than '+str(phone_len))

        user = self.model(email=self.normalize_email(email), phone=phone)
        user.set_password(passwrod)
        user.save()
        return user

    def create_superuser(self, email, phone, password):

        user = self.create_user(email, phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True)
    phone = models.CharField(db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_confirmed = models.BooleanField(default=False)
    phone_confirmed = models.BooleanField(default=False)

    first_name = models.CharField(
        db_index=True, max_length=255, blank=True, null=True)
    last_name = models.CharField(
        db_index=True, max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.phone.isdigit():
            raise TypeError('Phone must be a Digit.')

        phone_len = getattr(settings, 'PHONE_LEN', 9)
        if len(self.phone) < phone_len:
            raise TypeError('Phone length must be bigger than '+str(phone_len))

        super(User, self).save(*args, **kwargs)

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class Passport(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1

    GENDER_CHOICE = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    )

    name = models.CharField(max_length=150, null=False)
    surname = models.CharField(max_length=150, null=False)
    Patronymic = models.CharField(max_length=150, blank=True, default="")

    gender = models.IntegerField(choices=GENDER_CHOICE,
                                 default=GENDER_MALE)
    passport_series = models.IntegerField(null=False,
                                          validators=[
                                              RegexValidator(r'\d{4}')
                                          ])
    passport_number = models.IntegerField(null=False,
                                          validators=[
                                              RegexValidator(r'\d{6}')
                                          ])

    class Meta:
        verbose_name = 'Passport'
        verbose_name_plural = 'Passports'


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    passport = models.ForeignKey('Passport', on_delete=models.SET_NULL,
                                 null=True, related_name='user')
    ticket = models.ForeignKey('airline.Ticket', on_delete=models.SET_NULL,
                               null=True, related_name='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

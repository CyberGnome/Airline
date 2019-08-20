import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

        ordering = ['name']


class Region(models.Model):
    name = models.CharField(max_length=200, null=False)
    country = models.ForeignKey('Country', on_delete=models.PROTECT,
                                null=False, related_name='region')

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

        ordering = ['name']


class City(models.Model):
    name = models.CharField(max_length=200, null=False)
    region = models.ForeignKey('Region', on_delete=models.PROTECT,
                               null=False, related_name='city')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

        ordering = ['name']


class AircraftName(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Aircraft\'s Name'
        verbose_name_plural = 'Aircraft\'s Names'


class AircraftModel(models.Model):
    model = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Aircraft\'s Model'
        verbose_name_plural = 'Aircraft\'s Model'


class Aircraft(models.Model):
    name = models.ForeignKey('AircraftName', on_delete=models.PROTECT,
                             null=False, related_name='aircraft')
    model = models.ForeignKey('AircraftModel', on_delete=models.PROTECT,
                              null=True, related_name='aircraft')
    budget_places = models.IntegerField(default=0)
    vip_places = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Aircraft'
        verbose_name_plural = 'Aircraft'


class Flight(models.Model):
    FLIGHT_STATE_WAIT = 0
    FLIGHT_STATE_IN_PROCESS = 1
    FLIGHT_STATE_FINISHED = 2

    FLIGHT_STATE_CHOICE = (
        (FLIGHT_STATE_WAIT, 'Waiting'),
        (FLIGHT_STATE_IN_PROCESS, 'Processing'),
        (FLIGHT_STATE_FINISHED, 'Finished'),
    )

    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    departure_date = models.DateTimeField(null=False)
    arrival_date = models.DateTimeField(null=False)
    departure_point = models.OneToOneField('City', on_delete=models.PROTECT,
                                           null=False, related_name='dep_flight')
    arrival_point = models.OneToOneField('City', on_delete=models.PROTECT,
                                         null=False, related_name='arv_flight')
    aircraft = models.ManyToManyField('Aircraft', blank=True, default=[])
    state = models.IntegerField(choices=FLIGHT_STATE_CHOICE, default=FLIGHT_STATE_WAIT)

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

        ordering = ['departure_date', 'code']


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


class Ticket(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight = models.OneToOneField('Flight', on_delete=models.PROTECT,
                                  null=False)
    passenger = models.OneToOneField('Passport', on_delete=models.PROTECT,
                                     null=False)
    place = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    is_vip = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class User(AbstractUser):
    passport = models.ForeignKey('Passport', on_delete=models.SET_NULL,
                                 null=True, related_name='user')
    ticket = models.ForeignKey('Ticket', on_delete=models.SET_NULL,
                               null=True, related_name='user')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

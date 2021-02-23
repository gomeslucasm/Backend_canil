from django.db import models
""" from django.utils import timezone """
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, timezone, date


class Animal(models.Model):
    ''' Modelo que salva as informações de um animal '''
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='user')
    ANIMAL_TYPES = (
        ('C', 'Gato'),
        ('D', 'Cachorro'),
        ('H', 'Cavalo',),
        ('B', 'Ave'),
        ('O', 'Outro',)
    )
    animal_type = models.CharField(max_length=2, choices=ANIMAL_TYPES)
    birth_date = models.DateField()
    description = models.TextField(max_length=5000)
    SIZE = (
        ('PP', 'Muito pequeno'),
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
        ('GG', 'Muito grande')
    )
    size = models.CharField(max_length=2, choices=SIZE)
    show = models.BooleanField(default=True)
    # Canil information
    entry_date = models.DateField(auto_now_add=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    LOCATION = (
        ('C', 'Canil'),
        ('V', 'Voluntário')
    )
    location = models.CharField(max_length=1, choices=LOCATION, default='C')
    SEX = (
        ('M', 'Macho'),
        ('F', 'Fêmea')
    )
    sex = models.CharField(max_length=1, choices=SEX, default='M')
    responsible_volunteer = models.ForeignKey(get_user_model(
    ), on_delete=models.SET_NULL, blank=True, null=True, related_name='volunteer')
    is_castrated = models.BooleanField(default=False)
    is_adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['id']

    @property
    def age(self):
        """ Retora uma string com a idade do animal"""
        date = self.birth_date
        actual = date.today() - timedelta(hours=3)
        diff = relativedelta(actual, date)
        if diff.years > 0:
            if diff.years > 1:
                return str(diff.years) + ' anos'
            else:
                return str(diff.years) + ' ano'
        elif diff.months > 0:
            if diff.months > 1:
                return str(diff.months) + ' meses'
            else:
                return str(diff.months) + ' mês'
        elif diff.days > 1:
            return str(diff.days) + ' dias'
        else:
            return '1 dia'
    @property
    def adopted(self):
        return(self.model._meta.get_all_related_objects())

class AnimalPhoto(models.Model):
    """ Modelo que armazena as fotos para um determinado animal """
    default_img = 'default.jpeg'
    photo = models.ImageField(default=default_img)
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='animal_photo')

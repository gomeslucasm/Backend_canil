from django.db import models
from admin_animals.models import *
from django.contrib.auth import get_user_model


class Adopter(models.Model):
    ''' Modelo de adotante '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    cellphone = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    neighbourhood = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    document = models.CharField(max_length=100)

    class Meta:
        ordering = ["first_name"]

class Adoption(models.Model):
    ''' Modelo de adoção '''
    adoption_date = models.DateField(auto_now_add=True, blank = True)
    adopter = models.ForeignKey(Adopter, on_delete=models.SET_NULL, null=True, related_name = 'animal_adopter')
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, related_name = 'adopted_animal') 
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name = 'user_register_adoption')


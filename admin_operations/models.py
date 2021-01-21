from django.db import models
from admin_animals.models import Animal
from django.contrib.auth import get_user_model

class OperationType(models.Model):
    ''' Modelo que guarda o tipo de operação '''
    name = models.TextField(max_length=20)

    def __str__(self):
        return self.name

class Operation(models.Model):
    ''' Modelo que guarda informações sobre uma operação '''
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null= True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name = 'animal_operation')
    information = models.TextField(max_length = 1000)
    date = models.DateField(auto_now_add=True, blank = True)
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE, related_name = 'operation_types')

    def __str__(self):
        return self.information
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from admin_animals.private_serializers import *

class AdopterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopter
        fields = ('__all__')

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ('__all__')

class AdoptionJustWithAnimalInfoSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()

    class Meta:
        model = Adoption
        fields = ('animal')

class AdopterWithAnimalSerializer(serializers.ModelSerializer):
    
    animal_adopter = AdoptionJustWithAnimalInfoSerializer(many = True)
    animal = animal_adopter
    
    class Meta:
        model = Adopter
        fields = ('__all__')    



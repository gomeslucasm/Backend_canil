from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

# Default serializerss

class AnimalPhotoSerializer(serializers.ModelSerializer):
    ''' Serializador das fotos relacionadas a um animal '''
    class Meta:
        model = AnimalPhoto
        fields = ('photo','id','animal')

class AnimalSerializer(serializers.ModelSerializer):
    ''' Serializador do objeto animal '''
    animal_photo = AnimalPhotoSerializer(many=True, read_only = True)
    class Meta:
        model = Animal
        fields = [
            'id','animal_photo','animal_type','birth_date','description',
            'size','show','entry_date','death_date','code','location','sex',
            'is_castrated','is_adopted','responsible_volunteer','user','responsible_volunteer'
            ]
        extra_kwargs = {
            'animal_photo':{'required':False}
        }
    
    def create(self, validated_data):
        animal = Animal.objects.create(**validated_data)
        return animal

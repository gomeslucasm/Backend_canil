from rest_framework import serializers
from .models import *
from .private_serializers import AnimalPhotoSerializer



class PublicAnimalSerializer(serializers.ModelSerializer):
    ''' Serializador com as informações públicas dos animais '''

    location_display = serializers.CharField(source = 'get_location_display')
    size_display = serializers.CharField(source = 'get_size_display')
    sex_display = serializers.CharField(source = 'get_sex_display')
    animal_type_display = serializers.CharField(source = 'get_animal_type_display')
    animal_photo = AnimalPhotoSerializer(many = True)

    class Meta:
        model = Animal
        fields = (
            'id',
            'animal_type',
            'animal_type_display',
            'description',
            'size',
            'size_display',
            'location',
            'location_display',
            'age',
            'animal_photo',
            'show',
            'sex',
            'sex_display'
            )


from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

# Default serializerss

class AnimalPhotoSerializer(serializers.ModelSerializer):
    ''' Serializador das fotos relacionadas a um animal '''
    class Meta:
        model = AnimalPhoto
        fields = ('photo','id')

class AnimalSerializer(serializers.ModelSerializer):
    ''' Serializador do objeto animal '''
    animal_photo = AnimalPhotoSerializer(many=True)
    class Meta:
        model = Animal
        fields = ('__all__')
    
    def create(self, validated_data):
        animal_photos = validated_data.pop('animal_photo')
        animal = Animal.objects.create(validated_data)
        for animal_photo in animal_photos:
            AnimalPhoto.objects.create(animal = animal, **animal_photo)

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

# Default serializerss

class AnimalPhotoSerializer(serializers.ModelSerializer):
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

class OperationInfoSerializer(serializers.ModelSerializer):
    ''' 
    Serializador do objeto que retorna os dados sobre informações
    operações/serviços relacionados aos animais
     '''
    class Meta:
        model = OperationInfo
        fields = ('__all__')

class OperationSerializer(serializers.ModelSerializer):
    ''' 
    Serializador do objeto que retorna os nomes de operações/serviços
    '''
    class Meta:
        model = Operation
        fields = ('name',)

# Specific serilizers

class OperationWithInfoSerializer(serializers.ModelSerializer):
    operation_name = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='information'
     )
    class Meta:
        model = Operation
        fields = ('name','id','operation_name',)
        read_only_fields = ['operation_name',]

class OperationInfoWithNameSerializer(serializers.ModelSerializer):
    operation = serializers.StringRelatedField()
    class Meta:
        model = OperationInfo
        fields = ('operation','information','date')

    def create(self,validated_data):
        info = validated_data.pop('operation')



class AnimalWithOperationInfoSerializer(serializers.ModelSerializer):
    operation_animal = OperationInfoWithNameSerializer(many = True, read_only = True)

    class Meta:
        model = Animal
        fields = ('__all__')
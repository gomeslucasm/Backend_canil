from rest_framework import serializers
from .models import *
from admin_animals.private_serializers import AnimalSerializer

class OperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= OperationType
        fields= ('__all__')

class OperationSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    operation_type = OperationTypeSerializer()
    class Meta:
        model = Operation
        fields = ('__all__')

class OperationSerializerWithAnimal(serializers.ModelSerializer):
    animal = AnimalSerializer()
    class Meta:
        model = Operation
        fields = ('animal','date','information','user')

''' Serializador para obter as operações separadas por tipo '''
class OperationSeparatedByTypeSerializer(serializers.ModelSerializer):
    ''' Serializador para obter as operações separadas por tipo '''
    operation_types = OperationSerializerWithAnimal(many = True)
    operations = operation_types

    class Meta:
        model = OperationType
        fields = ('__all__')
        extra_kwargs = {
            'operation_types':'write_only',
            'operations':'read_only',
            }

class OperationWithNameSerializer(serializers.ModelSerializer):
    operation_type = OperationTypeSerializer()
    class Meta:
        model = Operation
        fields = ('__all__')

class OperationSeparatedByAnimalSerializer(serializers.ModelSerializer):

    animal_operation = OperationWithNameSerializer(many = True)
    operations = animal_operation

    class Meta:
        model = Animal
        fields = ('__all__')
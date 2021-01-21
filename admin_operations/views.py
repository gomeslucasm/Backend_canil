
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from .models import *
from django.shortcuts import get_object_or_404
from manage_users.permissions import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from admin_animals.models import Animal

# Create your views here.
class OperationViewSet(viewsets.ViewSet):  
    ''' 
    View que mostra e cadastra as operações/serviços realizados
     '''
    response = openapi.Response('Lista com as operações/serviços realizados', OperationSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna a lista das operações/serviços realizados
        '''
        queryset = Operation.objects.all()
        serializer = OperationSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response('Operação/serviço', OperationSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna uma operação/serviço específico
         '''
        queryset = Operation.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = OperationSerializer(query)
        return Response(serializer.data)

    response = openapi.Response('Operação/serviço criado', OperationSerializer)
    @swagger_auto_schema(responses = {201:response})
    def create(self,request):
        ''' 
        Adiciona um novo animal
        '''
        data = request.data
        data['user'] = request.user.id
        serializer = AnimalSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OperationTypeViewSet(viewsets.ViewSet):  
    ''' 
    View que mostra e cadastra os tipos de operações/serviços
    '''
    response = openapi.Response(
        'Tipos de operações/serviços cadastradas', 
        OperationTypeSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna a lista dos tipos de operações cadastradas
        '''
        queryset = OperationType.objects.all()
        serializer = OperationTypeSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response(
        'Tipo de operação', 
        OperationTypeSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna um tipo de operação cadastrada
         '''
        queryset = OperationType.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = OperationTypeSerializer(query)
        return Response(serializer.data)

    def create(self,request):
        ''' 
        Adiciona um novo tipo de operação
        '''
        data = request.data
        data['user'] = request.user.id
        serializer = OperationTypeSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OperationSeparatedByTypeViewSet(viewsets.ViewSet):  
    ''' 
    View que mostra as operações/serviços separados pelos tipos
    '''
    response = openapi.Response('Operações/serviços separados por tipo', OperationSeparatedByTypeSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna a lista das operações/serviços separados por tipo
        '''
        queryset = OperationType.objects.all()
        serializer = OperationSeparatedByTypeSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response('Operações/serviços de apenas um tipo', OperationSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna as operações/serviços de apenas um tipo
         '''
        queryset = OperationType.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = OperationSeparatedByTypeSerializer(query)
        return Response(serializer.data)

class OperationSeparatedByAnimalViewSet(viewsets.ViewSet):  
    ''' 
    View que mostra as operações/serviços separados por animal
     '''
    response = openapi.Response('Operações/serviços separados por animal', OperationSeparatedByAnimalSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna a lista das operações/serviços separados por animal
        '''
        queryset = Animal.objects.all()
        serializer = OperationSeparatedByAnimalSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response('Operações/serviços para um animal', OperationSeparatedByAnimalSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna a lista das operações/serviços para um animal
         '''
        queryset = Animal.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = OperationSeparatedByAnimalSerializer(query)
        return Response(serializer.data)
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .private_serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from .models import *
from django.shortcuts import get_object_or_404
from manage_users.permissions import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Basic views

class AnimalViewSet(viewsets.ViewSet):  
    ''' 
    View que retorna inforções sobre os animais
     '''
    animal_response = openapi.Response('Lista dos animais', AnimalSerializer(many = True))
    @swagger_auto_schema(responses={200: animal_response}) 
    def list(self, request):
        ''' 
        Retorna a lista dos animais
        '''
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset,many = True)
        return Response(serializer.data)

    animal_response = openapi.Response('Informações do animal', AnimalSerializer)
    @swagger_auto_schema(responses = {200:animal_response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna um animal específico utilizando a chave do model
         '''
        queryset = Animal.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = AnimalSerializer(query)
        return Response(serializer.data)

    animal_response = openapi.Response('Retorna o animal criado', AnimalSerializer)
    @swagger_auto_schema(request_body=AnimalSerializer, responses = {201:animal_response})
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
    
    def get_permissions(self):
        """
        Permissões para o acesso da view
        tem que estar logado para acessar todas as views
        """
        permission_classes = [IsUser]
        return [permission() for permission in permission_classes]

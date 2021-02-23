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
from rest_framework.permissions import AllowAny
from manage_users.permissions import *

class AdopterViewSet(viewsets.ViewSet):  
    ''' 
    View que retorna os adotantes
     '''
    response = openapi.Response('Lista dos animais', AdopterSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna a lista dos adotantes
        '''
        queryset = Adopter.objects.all()
        serializer = AdopterSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response('Informações do Adopter', AdopterSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna um adotante específico utilizando a chave do model
         '''
        queryset = Adopter.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = AdopterSerializer(query)
        return Response(serializer.data)

    response = openapi.Response('Retorna o Adopter criado', AdopterSerializer)
    @swagger_auto_schema(request_body=AdopterSerializer, responses = {201:response})
    def create(self,request):
        ''' 
        Adiciona um novo Adopter
        '''
        data = request.data
        data['user'] = request.user.id
        serializer = AdopterSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    ''' def get_permissions(self):
        """
        Permissões para o acesso da view
        tem que estar logado para acessar todas as views
        """
        permission_classes = [IsUser]
        return [permission() for permission in permission_classes] '''

class AdoptionViewSet(viewsets.ViewSet):  
    ''' 
    View que retorna as adoções
     '''
    response = openapi.Response('Lista dos animais', AdopterSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna a lista as adoções
        '''
        queryset = Adopter.objects.all()
        serializer = AdopterSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response('Informações da adoção', AdoptionSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna uma adoção específica
        '''

        queryset = Adopter.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = AdopterSerializer(query)
        return Response(serializer.data)

    response = openapi.Response('Retorna a adoção criada', AdoptionSerializer)
    @swagger_auto_schema(request_body=AdoptionSerializer, responses = {201:response})
    def create(self,request):
        ''' 
        Adiciona uma nova Adoção
        '''
        data = request.data
        data['user'] = request.user.id
        animal_id = data['animal'][id]
        # Atualizando o modelo do animal para adotado
        animal = Animals.objects.get(id = id)
        animal.is_adopted = True
        animal.save()
        # Passando os dados para o serializador
        serializer = AdoptionSerializer(data = data)
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

class AdopterWithAnimalViewSet(viewsets.ViewSet):  
    ''' 
    View que retorna as adoções
     '''
    response = openapi.Response('Lista dos adotantes e seus animais', AdopterWithAnimalSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna os adotantes com os respectivos animais adotados
        '''
        queryset = Adopter.objects.all()
        serializer = AdopterWithAnimalSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response('Informações do adotante e seus animais', AdopterWithAnimalSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna um adotante específico com os respectivos animais adotados
        '''
        queryset = Adopter.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = AdopterWithAnimal(query)
        return Response(serializer.data)

class AdoptionViewSet(viewsets.ViewSet):  
    ''' 
    View que retorna as adoções
     '''
    response = openapi.Response('Lista dos adotantes e seus animais', AdopterWithAnimalSerializer(many = True))
    @swagger_auto_schema(responses={200: response}) 
    def list(self, request):
        ''' 
        Retorna os adotantes com os respectivos animais adotados
        '''
        queryset = Adoption.objects.all()
        serializer = AdoptionSerializer(queryset,many = True)
        return Response(serializer.data)

    response = openapi.Response('Informações do adotante e seus animais', AdopterWithAnimalSerializer)
    @swagger_auto_schema(responses = {200:response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna um adotante específico com os respectivos animais adotados
        '''
        queryset = Adoption.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = AdoptionSerializer(query)
        return Response(serializer.data)
    
    def create(self,request):
        data = request.data
        data['user'] = request.user
        serializer = AdoptionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def get_permissions(self):
        ''' Permissões para o acesso da view
        tem que estar logado para acessar todas as views '''
        permission_classes = [IsUser]
        return [permission() for permission in permission_classes]
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
    animal_response = openapi.Response('Descrição da resposta', AnimalSerializer(many = True))
    @swagger_auto_schema(responses={200: animal_response}) 
    def list(self, request):
        ''' 
        Retorna a lista dos animais
        '''
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset,many = True)
        return Response(serializer.data)

    animal_response = openapi.Response('Descrição da resposta', AnimalSerializer)
    @swagger_auto_schema(responses = {200:animal_response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna um animal específico utilizando a chave do model
         '''
        queryset = Animal.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = AnimalSerializer(query)
        return Response(serializer.data)

    animal_response = openapi.Response('Descrição da resposta', AnimalSerializer(many = True))
    @swagger_auto_schema(request_body=AnimalSerializer, response = {201:animal_response})
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

class OperationViewSet(viewsets.ViewSet):
    ''' 
    View que retorna dados sobre as operações e servições
     '''
    operation_response = openapi.Response('Descrição da resposta', OperationSerializer(many = True))
    @swagger_auto_schema(responses = {200:operation_response})
    def list(self, request):
        ''' 
        Retorna os tipos de operações listadas 
        '''
        queryset = Operation.objects.all()
        serializer = OperationSerializer(queryset,many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ''' 
        Retorna uma operação específica (não está listada nos urls) 
        '''
        queryset = Operation.objects.all()
        query = get_object_or_404(queryset , pk=pk)
        serializer = OperationSerializer(query)
        return Response(serializer.data)

    operation_response = openapi.Response('Descrição da resposta', OperationSerializer) 
    @swagger_auto_schema(
        request_body = OperationSerializer, 
        responses = {200:operation_response},)
    def create(self,request):
        ''' 
        Adicionando uma nova operação
        '''
        data = request.data
        serializer = OperationSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        """
        Permissões para o acesso da view
        list,retrieve - Todos os usuários
        create - Usuário staff ou veterinary 
        """
        if self.action == 'create':
            permission_classes = [IsStaffUser|IsVeterinary]
        else:
            permission_classes = [IsUser]
        return [permission() for permission in permission_classes]





class OperationInfoViewSet(viewsets.ViewSet):
    ''' 
    View que retorna as operações com as informações referentes
    '''
    operation_info_response = openapi.Response('Descrição da resposta', OperationInfoSerializer(many = True)) 
    @swagger_auto_schema(responses = {200:operation_info_response},)
    def list(self, request):
        ''' 
        Retorna as informações sobre todas as operações
        realizada em todos os animais
        '''
        queryset = OperationInfo.objects.all()
        serializer = OperationInfoSerializer(queryset,many = True)
        return Response(serializer.data)
    
    operation_info_response = openapi.Response('Descrição da resposta', OperationInfoSerializer) 
    @swagger_auto_schema(responses = {200:operation_info_response},)
    def retrieve(self, request, pk=None):
        ''' 
        Retorna as informações sobre uma operação específica
        realizada em todos os animais
        '''
        queryset = Operation.objects.all()
        query = get_object_or_404(queryset , pk=pk)
        serializer = OperationWithInfoSerializer(query)
        return Response(serializer.data)

    operation_info_response = openapi.Response('Descrição da resposta', OperationInfoSerializer) 
    @swagger_auto_schema(request_body = OperationInfoSerializer,responses = {200:operation_info_response},)
    def create(self,request):
        data = request.data
        data['user'] = request.user.id
        instance = OperationInfoSerializer(data = data)
        if instance.is_valid():
            model = instance.save()
            return Response(data = instance.data,status = status.HTTP_201_CREATED)
        return Response(instance.errors, status = status.HTTP_201_CREATED)

        

class AnimalWithOperationInfoViewSet(viewsets.ViewSet):
    ''' 
    Viewset
     '''
    data = openapi.Response('Descrição da resposta', AnimalWithOperationInfoSerializer(many=True)) 
    @swagger_auto_schema(responses = {200:data},) 
    def list(self, request):
        queryset = Animal.objects.all()
        serializer = AnimalWithOperationInfoSerializer(queryset,many = True)
        return Response(serializer.data)

    data = openapi.Response('Descrição da resposta', AnimalWithOperationInfoSerializer()) 
    @swagger_auto_schema(responses = {200:data},) 
    def retrieve(self, request, pk=None):
        queryset = Animal.objects.all()
        query = get_object_or_404(queryset , pk=pk)
        serializer = AnimalWithOperationInfoSerializer(query)
        return Response(serializer.data)

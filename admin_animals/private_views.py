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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = AnimalSerializer(data,many = True) 

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        

        return Response({
                'data':serializer.data,
                'nextPage':nextPage,
                'previousPage':previousPage,
            })

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

    def destroy(self, request, pk=None):
        queryset = Animal.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        query = query.delete()
        ''' import ipdb;ipdb.set_trace(); '''
        return Response(status = status.HTTP_200_OK)
        


    animal_response = openapi.Response('Retorna o animal criado', AnimalSerializer)
    @swagger_auto_schema(request_body=AnimalSerializer, responses = {201:animal_response})
    def create(self,request):
        ''' 
        Adiciona um novo animal
        '''
        
        data = request.data
        data['user'] = 1
        exclude_keys = []
        animal_photos = list()
        for key in data:
            if key[0:12] == 'animal_photo':
                animal_photos.append(data[key])
                exclude_keys.append(key)

        for key in exclude_keys:
            data.pop(key)

        

        try:
            data['responsible_volunteer'] = int(data['responsible_volunteer'])
        except:
            data.pop('responsible_volunteer')

        serializer = AnimalSerializer(data = data)
        
        """ import ipdb;ipdb.set_trace() """
        if serializer.is_valid():
            animal = serializer.save()
            for animal_photo in animal_photos:
                serializer = AnimalPhotoSerializer(data = {'animal':animal.id,'photo':animal_photo,})
                if serializer.is_valid():
                    serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
'''  def get_permissions(self):

Permissões para o acesso da view
tem que estar logado para acessar todas as views

permission_classes = [IsUser]
return [permission() for permission in permission_classes] '''

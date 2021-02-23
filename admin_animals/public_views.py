from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .public_serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from .models import *
from django.shortcuts import get_object_or_404
from manage_users.permissions import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Basic views

class AnimalViewSet(viewsets.ViewSet):  
    ''' 
    View que retorna informações sobre os animais
     '''
    animal_response = openapi.Response('Descrição da resposta', PublicAnimalSerializer(many = True))
    @swagger_auto_schema(responses={200: animal_response}) 
    def list(self, request):
        ''' 
        Retorna a lista dos animais
        '''
        query_request = request.GET
        queryset = Animal.objects.filter(show = True)
    
       #for key in query_request.keys():
        #    query_filters = query_request[key]
         #   query_filters = query_filters.split('-')
        #    expression = list()
         #   for query_filter in query_filters:
         #       expression.append('Q(' + key + '= "' + query_filter + '")')    
         #   print('|'.join(expression))
         #   queryset = queryset.filter(eval('|'.join(expression)))
         #   print(queryset) 

        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 4)
        ''' import ipdb;ipdb.set_trace(); '''

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = PublicAnimalSerializer(data,many = True) 

        if data.has_next():
            nextPage = data.next_page_number()
        else:
            nextPage = data.has_next()

        if data.has_previous():
            previousPage = data.previous_page_number()
        else:
            previousPage = data.has_previous()
        ''' import ipdb;ipdb.set_trace() '''
        return Response({
                'data':serializer.data,
                'nextPage':nextPage,
                'prevPage':previousPage,
                'pages':list(iter(paginator.page_range)),
                'currentPage':page,
            })



    animal_response = openapi.Response('Descrição da resposta', PublicAnimalSerializer)
    @swagger_auto_schema(responses = {200:animal_response})
    def retrieve(self, request, pk=None):
        ''' 
        Retorna um animal específico utilizando a chave do model
         '''
        queryset = Animal.objects.filter(show = True)
        query = get_object_or_404(queryset, pk=pk)
        serializer = PublicAnimalSerializer(query)
        return Response(serializer.data)


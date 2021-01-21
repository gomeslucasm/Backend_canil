from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from .permissions import IsVeterinary
from .models import NewUser

class StaffUserView(viewsets.ViewSet):
    ''' View que retorna informações de usuários staff '''
    def list(self, request):
        ''' Retorna a lista de usuários staff'''
        queryset = NewUser.objects.all().filter(is_staff=True)
        serializer = StaffUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ''' Retorna um usuário staff específico'''
        queryset = NewUser.objects.all().filter(is_staff=True)
        user = get_object_or_404(queryset, pk=pk)
        serializer = StaffUserSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        ''' Cria um usuário staff específico'''
        serializer = StaffUserSerializer(data = request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class VeterinaryUserView(viewsets.ViewSet):
    ''' View que retorna informações de usuários veterináriso '''
    def list(self, request):
        ''' Retorna a lista de usuários veterinários'''
        queryset = NewUser.objects.all().filter(is_veterinary=True)
        serializer = VeterinaryUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ''' Retorna um usuário veterinário específico '''
        queryset = NewUser.objects.all().filter(is_veterinary=True)
        user = get_object_or_404(queryset, pk=pk)
        serializer = VeterinaryUserSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        ''' Cria um usuário de veterinário '''
        serializer = VeterinaryUserSerializer(data = request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class VolunteerUserView(viewsets.ViewSet):
    ''' View que retorna informações de usuários veterinary '''
    def list(self, request):
        ''' Retorna a lista de voluntários '''
        queryset = NewUser.objects.all().filter(is_volunteer=True)
        serializer = VolunteerUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ''' Retorna um voluntário em específico '''
        queryset = NewUser.objects.all().filter(is_volunteer=True)
        user = get_object_or_404(queryset, pk=pk)
        serializer = VolunteerUserSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        ''' Cria um usuário de voluntário '''
        serializer = VolunteerUserSerializer(data = request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserView(viewsets.ViewSet):
    ''' View que retorna informações de usuários veterinary '''
    def list(self, request):
        ''' Retorna a lista de voluntários '''
        queryset = NewUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ''' Retorna um voluntário em específico '''
        queryset = NewUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

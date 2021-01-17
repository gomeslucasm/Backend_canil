from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StaffUserSerializer,VolunteerUserSerializer,VeterinaryUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from .permissions import IsVeterinary

class StaffUserCreate(APIView):
    permission_classes = [IsVeterinary,]
    def post(self, request):
        serializer = StaffUserSerializer(data = request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class VolunteerUserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = VolunteerUserSerializer(data = request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class VeterinaryUserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = VeterinaryUserSerializer(data = request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

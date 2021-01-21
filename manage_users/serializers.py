from rest_framework import serializers
from .models import NewUser
from django.contrib.auth import get_user_model

class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','username','first_name','last_name','cellphone','password',
        'is_staff','is_volunteer','is_veterinary')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff':{'read_only': True},
            'is_volunteer':{'read_only': True},
            'is_veterinary':{'read_only': True},
            'is_superuser':{'read_only': True},
            }

    def create(self, validated_data,**kwargs):
        model = self.Meta.model.objects.create_staff_user(**validated_data)
        model.save()
        return model

class VolunteerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','username','first_name','last_name','cellphone','password')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff':{'read_only': True},
            'is_volunteer':{'read_only': True},
            'is_veterinary':{'read_only': True},
            'is_superuser':{'read_only': True},
            }

    def create(self, validated_data,**kwargs):
        model = self.Meta.model.objects.create_volunteer_user(**validated_data)
        model.save()
        return model

class VeterinaryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','username','first_name','last_name','cellphone','password')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff':{'read_only': True},
            'is_volunteer':{'read_only': True},
            'is_veterinary':{'read_only': True},
            'is_superuser':{'read_only': True},
            }

    def create(self, validated_data,**kwargs):
        model = self.Meta.model.objects.create_veterinary_user(**validated_data)
        model.save()
        return model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','username','first_name','last_name','cellphone','password')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff':{'read_only': True},
            'is_volunteer':{'read_only': True},
            'is_veterinary':{'read_only': True},
            'is_superuser':{'read_only': True},
            }


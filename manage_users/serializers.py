from rest_framework import serializers
from .models import NewUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
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

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    ''' @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name + user.last_name
        token['id'] = user.id
        # ...

        return token '''
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['id'] = self.user.id
        data['name'] = self.user.first_name + ' ' + self.user.last_name

        return data

from rest_framework.permissions import IsAuthenticated
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = NewUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As 2 senhas não conferem"})
        if attrs['old_password'] == attrs['password']:
            raise serializers.ValidationError({"password": "Senha nova igual a antiga"})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
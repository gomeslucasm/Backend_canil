from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


class CustomUserManager(BaseUserManager):

    def create_user(self,email,username,password,first_name,
                        last_name,cellphone,**other_fields):
    
        user = self.model(email = email, username = username, first_name = first_name,
                        last_name = last_name, cellphone = cellphone,**other_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,email,username,password,first_name,
                        last_name,cellphone,**other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_veterinary', True)
        other_fields.setdefault('is_volunteer', True)

        return self.create_user(email,username,password,first_name,
                        last_name,cellphone,**other_fields)

    def has_module_perms(self, app_label):
        return self.is_superuser
           
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def create_staff_user(self, email, username, first_name, last_name, password,
                            cellphone, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_veterinary', False)
        other_fields.setdefault('is_volunteer', False)

        email = self.normalize_email(email)

        return self.create_user(email,username,password,first_name,
                        last_name,cellphone,**other_fields)
    
    def create_veterinary_user(self, email, username, first_name, last_name, password,
                        cellphone, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_veterinary', True)
        other_fields.setdefault('is_volunteer', False)
        other_fields.setdefault('is_superuser', True)

        email = self.normalize_email(email)
        user = self.model(email = email, username = username, first_name = first_name,
                        last_name = last_name, cellphone = cellphone, **other_fields)

        return self.create_user(email,username,password,first_name,
                        last_name,cellphone,**other_fields)
    
    def create_volunteer_user(self, email, username, first_name, last_name, password,
                        cellphone, **other_fields):
    
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_veterinary', False)
        other_fields.setdefault('is_volunteer', True)

        email = self.normalize_email(email)
        user = self.model(email = email, username = username, first_name = first_name,
                        last_name = last_name, cellphone = cellphone, **other_fields)

        return self.create_user(email,username,password,first_name,
                        last_name,cellphone,**other_fields)

class NewUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    username  = models.CharField(max_length=50, unique = True)
    email = models.EmailField(max_length=40, unique=True)
    cellphone = models.CharField(max_length=12)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_volunteer = models.BooleanField(default = False)
    is_veterinary = models.BooleanField(default = False)
    date_joined = models.DateTimeField(default=timezone.now)
 
    objects = CustomUserManager()
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name','cellphone']
 
    def __str__(self):

        return self.first_name + ' ' + self.last_name
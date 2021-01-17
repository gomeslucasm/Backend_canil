from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    list_display = ('username',)

admin.site.register(NewUser,UserAdminConfig)
# Register your models here.

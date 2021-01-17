from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(AnimalPhoto)
class AnimalPhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass
@admin.register(OperationInfo)
class OperationInfoAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(OperationType)
class  OperationTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Operation)
class  OperationAdmin(admin.ModelAdmin):
    pass
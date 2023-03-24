from django.contrib import admin
from . models import studentform

@admin.register(studentform)
class studenformadmin(admin.ModelAdmin):
    list_display=["name","email","password"]

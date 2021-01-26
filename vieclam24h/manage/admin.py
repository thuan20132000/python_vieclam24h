from django.contrib import admin
from .models import Category
# Register your models here.



class AdminCategory(admin.ModelAdmin):
    pass


admin.site.register(Category)
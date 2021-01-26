from django.contrib import admin
from .models import Category,Occupation
# Register your models here.



class AdminCategory(admin.ModelAdmin):
    pass


admin.site.register(Category)




class AdminOccupation(admin.ModelAdmin):
    pass

admin.site.register(Occupation)
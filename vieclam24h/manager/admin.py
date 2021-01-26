from django.contrib import admin
from .models import Category,Occupation,Job,JobImages
# Register your models here.



class AdminCategory(admin.ModelAdmin):
    pass


admin.site.register(Category)




class AdminOccupation(admin.ModelAdmin):
    pass

admin.site.register(Occupation)


class JobImageInline(admin.StackedInline):
    model = Job
    max_num = 10
    extra = 0


class AdminJob(admin.ModelAdmin):
    inlines = [JobImageInline]

admin.site.register(Job)
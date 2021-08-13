from django.contrib import admin
from .models import *


# Register your models here.
class cateadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(categ, cateadmin)


class prodadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','img','stock','available']
    list_editable = ['price','stock','img','available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(products,prodadmin)

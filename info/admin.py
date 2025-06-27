from django.contrib import admin
from .models import  Contact 
from django.contrib.admin.options import ModelAdmin


# Register your models here.


class ContactAdmin(ModelAdmin):
	list_display = ['first_name', 'second_name' , 'mobile' , 'email', 'message' , 'date']
	search_field = ['first_name' ,  'mobile' , 'email',]
	list_filter = [ 'mobile' , 'email',]

admin.site.register(Contact, ContactAdmin)


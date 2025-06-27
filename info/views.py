from django.shortcuts import render
from info.models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
#from django.views.generic import  DetailView  # importing class based views from views.generic
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView # importing class based views from views.generic
from django.core.paginator import Paginator
from django.urls import reverse_lazy 



# Create your views here.  

#home_view
def home(request):
    return render(request, 'info/index.html') 

def about(request):
	return render(request, 'info/about.html')


#product view for frontend

def product(request):
	return render(request, 'info/admission.html')



#shop view for frontend

def shop(request):
	return render(request, 'info/shop.html')


#contact view for website 

class ContactView(CreateView):
	model = Contact
	fields = ['first_name', 'second_name' , 'to_the_department',  'email' , 'mobile' , 'message' ] #describe the field need to create 
	success_url = reverse_lazy('home')



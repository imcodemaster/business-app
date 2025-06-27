from django.shortcuts import render 
from .models import * 
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
 # importing class based views from views.generic
from django.views.generic import View, ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #importing loginrequiredMixin and UserPassesTestMixin from auth.mixin
from django.contrib.auth.models import User #import User from models
from django.urls import reverse_lazy , reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect 
from django.views import View
import requests

def home (request):
    return render(request, 'todo/index.html')


class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'todo/task_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'task' , 'user'
    ordering = ['-published']
    paginate_by = 10


    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'todo/task_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(Task, id = self.kwargs['pk'])
        context = super(TaskDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'task'
        return context
    



class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task #describing models 
    fields = ['taskname', 'task_descriptions' , 'initiate' , 'complete' , 'Task_highlight' ] #describe the field need to create 
    success_url = reverse_lazy('task-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Task
    fields = ['taskname', 'task_descriptions' , 'initiate' , 'complete' , 'Task_highlight' ] #describe the field need to Update
    success_url = reverse_lazy('task-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        task = self.get_object()

        if self.request.user == task.author:
            return True
        return False 

class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Task
    success_url = reverse_lazy('task-list')

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False 


#=================================================
#=================================================
class TaskCommentCreateView(LoginRequiredMixin, CreateView):
    model = TaskComment #describing models 
    fields = ['comment_content'] #describe the field need to create 
    #ordering = ['published']
    template_name = 'todo/taskcomment_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self,form):
        form.instance.task_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)



class weekprojectListView(LoginRequiredMixin,ListView):
    model = WeekProject
    template_name = 'todo/weekproject_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'weekproject'
    ordering = ['-published']
    paginate_by = 10 # pagination  (django provided )


    def get_queryset(self):
        return WeekProject.objects.filter(author=self.request.user)


class weekprojectCreateView(LoginRequiredMixin, CreateView):
    model = WeekProject #describing models 
    fields = ['job' , 'job_descriptions' ,  'weekproject_highlight' , 'initiate' , 'halfway' , 'complete'] #describe the field need to create 
    success_url = reverse_lazy('weekproject-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class weekprojectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = WeekProject
    fields = ['job' , 'job_descriptions' , 'weekproject_highlight', 'initiate' , 'halfway' , 'complete'] #describe the field need to Update
    success_url = reverse_lazy('weekproject-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        weekproject = self.get_object()

        if self.request.user == weekproject.author:
            return True
        return False 

class weekprojectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = WeekProject
    success_url = reverse_lazy('weekproject-list')

    def test_func(self):
        weekproject = self.get_object()
        if self.request.user == weekproject.author:
            return True
        return False 



class weekprojectDetailView(LoginRequiredMixin,DetailView):
    model = WeekProject
    template_name = 'todo/weekproject_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(WeekProject, id = self.kwargs['pk'])
        context = super(weekprojectDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'weekproject'
        return context
    
#==============================================

class EventListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'todo/event_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'event' , 'user'
    ordering = ['-published']
    paginate_by = 10


    def get_queryset(self):
        return Event.objects.filter(author=self.request.user)


class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event
    template_name = 'todo/event_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(Event, id = self.kwargs['pk'])
        context = super(EventDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'event'
        return context
    



class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event #describing models 
    fields = ['eventname', 'event_descriptions' , 'eventon' , 'complete' , 'event_highlight' ] #describe the field need to create 
    success_url = reverse_lazy('event-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Event
    fields = ['eventname', 'event_descriptions' , 'eventon' , 'complete' , 'event_highlight' ] #describe the field need to create 
    success_url = reverse_lazy('event-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        task = self.get_object()

        if self.request.user == task.author:
            return True
        return False 

class EventDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Event 
    success_url = reverse_lazy('event-list')

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False 


#=================================================
#=================================================


class WalletListView(LoginRequiredMixin,ListView):
    model = Wallet
    template_name = 'todo/wallet_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'wallet' , 'user'
    ordering = ['-published']
    paginate_by = 10


    def get_queryset(self):
        return Wallet.objects.filter(author=self.request.user)


class WalletUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Wallet
    fields = ['person_name' ] #describe the field need to create 
    success_url = reverse_lazy('wallet-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        wallet = self.get_object()

        if self.request.user == wallet.author:
            return True
        return False 

class WalletDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Wallet 
    success_url = reverse_lazy('wallet-list')

    def test_func(self):
        wallet = self.get_object()
        if self.request.user == wallet.author:
            return True
        return False 

class WalletCreateView(LoginRequiredMixin, CreateView):
    model = Wallet #describing models 
    fields = ['person_name' ] #describe the field need to create 
    success_url = reverse_lazy('wallet-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WalletDetailView(LoginRequiredMixin,DetailView):
    model = Wallet
    template_name = 'todo/wallet_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(Wallet, id = self.kwargs['pk'])
        context = super(WalletDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'wallet'
        return context
    

#=================================================
#=================================================
class TransistionCreateView(LoginRequiredMixin, CreateView):
    model = Transistion #describing models 
    fields = ['payment_status' , 'payment_mode' , 'comment' , 'amount'] #describe the field need to create 
    #ordering = ['published']
    template_name = 'todo/transistion_form.html'
    success_url = reverse_lazy('wallet-list')

    def form_valid(self,form):
        form.instance.wallet_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    template_name = 'todo/notes_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'notes' , 'user'
    ordering = ['-published']
    paginate_by = 10


    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes #describing models 
    fields = ['note' ] #describe the field need to create 
    success_url = reverse_lazy('notes-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NotesDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Notes
    success_url = reverse_lazy('notes-list')

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False 

#=================================================
from django.shortcuts import render
from .models import * 
from django.shortcuts import get_object_or_404

#from django.contrib.auth.decorators import login_required
 # importing class based views from views.generic
from django.views.generic import View, ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #importing loginrequiredMixin and UserPassesTestMixin from auth.mixin
from django.contrib.auth.models import User #import User from models
from django.urls import reverse_lazy , reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .render import Render
from django.views import View




def LikeView(request , pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    got_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        got_liked = False
    else:
        post.likes.add(request.user)
        got_liked = True
    return HttpResponseRedirect(reverse('post-detail' , args=[str(pk)]))

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'post' , 'user'
    ordering = ['-published']
    paginate_by = 10


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post/post_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        got_liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            got_liked = True

        context = super(PostDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'post'
        context ['total_likes'] = total_likes
        context ['got_liked'] = got_liked
        return context
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post #describing models 
    fields = ['subject', 'about' , 'content' , 'content_addition' , 'highlight' ,"image"  ] #describe the field need to create 
    success_url = reverse_lazy('post-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Post
    fields = ['subject', 'about' , 'department' , 'course' , 'semester' , 'subjects' , 'content' ,'content_addition', 'highlight' ,"image"  ] #describe the field need to Update
    success_url = reverse_lazy('post-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False 

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 



def postsearch(request):

    try:
        query = request.GET.get('querypost')
    except:
        query = None

    if query :
        query = request.GET.get('querypost').lower()
        template = 'post/postresults.html'
        postresult = [item for item in Post.objects.filter(course__icontains = query) if query in item.course.lower()]



    else:
        template = 'post/post-list.html'
        postresult = {}

    return render(request, template, {"postresult": postresult })


#=================================================
def OrderList(request):
    order = order_list.objects.filter(user = request.user)
    return render(request,"../templates/post/order_list.html", {"order":order})


#=================================================

class MyOrderView(CreateView):
	model = myorder
	fields = ['first_name', 'second_name' , 'item',  'company' , 'date' , 'mobile' , 'message' ] #describe the field need to create 
	success_url = reverse_lazy('home')

#===================================================


class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = PostComment #describing models 
    fields = ['comment_content'] #describe the field need to create 
    #ordering = ['published']
    template_name = 'post/postcomment_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

class TicketListView(ListView):
    model = Ticket
    template_name = 'info/story_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'story'
    ordering = ['-published']
    paginate_by = 50 # pagination  (django provided )





class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket #describing models 
    fields = ['subject' , 'message'] #describe the field need to create 
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TicketUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Ticket
    fields = ['subject' ] #describe the field need to Update
    success_url = reverse_lazy('ticket-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False 

class TicketDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Ticket
    success_url = 'blog/ticket/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 



class listpdfView(View):

    def get(self, request):
        list = pooja_list.objects.filter(user = request.user)
        today = timezone.now()
    
        params = {
            'today': today,
            'fees': list,
            'request': request
            }
        return Render.render( '../templates/post/fees_pdf.html',  params)    



class orderlistpdfView(View):

    def get(self, request):
        order = order_list.objects.filter(user = request.user)
        today = timezone.now()
    
        params = {
            'today': today,
            'order': order,
            'request': request
            }
        return Render.render( '../templates/post/order_list_pdf.html',  params)    


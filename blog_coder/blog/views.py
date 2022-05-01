from django.shortcuts import render
from blog.models import *
from blog.forms import *

# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    
    posts = Posts.objects.all()

    return render(request, 'blog/home.html', {"title": "Home", "message": "Título del blog", "posts": posts})

def about(request):

    return render(request, 'blog/about.html', {"title": "Acerca de este blog"})
class PostsList(ListView):

    model = Posts
    template_name = "blog/posts_list.html"

class PostDetail(DetailView):

    model = Posts
    template_name = "blog/posts_detail.html"

class PostCreate(CreateView):

    model = Posts
    success_url = "/pages/"
    fields = ['title', 'subtitle', 'body', 'author', 'date', 'image']

class PostUpdate(UpdateView):

    model = Posts
    success_url = "/pages/"
    fields = ['title', 'subtitle', 'body']

class PostDelete(DeleteView):

    model = Posts
    success_url = "/pages/"
    
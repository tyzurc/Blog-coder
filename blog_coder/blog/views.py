from django.shortcuts import render, redirect
from blog.models import *
from accounts.models import Avatar
from blog.forms import *

# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    # Tira error si el user no tiene avatar todavía
    """    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        
        return render(request, 'blog/home.html', {"title": "Home", "message": "¡Bienvenidx!", "image_url": imagen})
    """
    return render(request, 'blog/home.html', {"title": "Home", "message": "¡Bienvenidx!"})

def about(request):

    return render(request, 'blog/about.html', {"title": "Acerca de mí"})
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
    
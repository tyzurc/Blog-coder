from django.shortcuts import render, redirect
from blog.models import *
from accounts.models import Avatar
from blog.forms import *

# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Django authentication

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        return render(request, 'blog/home.html', {"title": "Home", "message": "¡Bienvenidx!", "image_url": imagen})
    
    return render(request, 'blog/home.html', {"title": "Home", "message": "¡Bienvenidx!"})

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
    
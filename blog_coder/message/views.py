from django.dispatch import receiver
from django.shortcuts import render
from message.models import *
from message.forms import *

# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

# Django authentication

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MessagesList(LoginRequiredMixin, ListView):

    model = Message
    template_name = "message/message_list.html"

class MessageDetail(LoginRequiredMixin, DetailView):

    model = Message
    template_name = "message/message_detail.html"

class MessageCreate(LoginRequiredMixin, CreateView):

    model = Message
    success_url = "/messages/"
    fields = ['title','sender', 'reciever', 'content', 'date']


class MessageDelete(LoginRequiredMixin, DeleteView):

    model = Message
    success_url = "/messages/"
    
from django.urls import path
from blog.views import *

urlpatterns = [

    path('', PostsList.as_view(), name="Posts")
    
]

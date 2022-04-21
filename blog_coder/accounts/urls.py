from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', register_request, name="register"),
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    #path('profile/',),
    path('update/', update_user, name="update_user"),
]

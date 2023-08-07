from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register_url'),
    path('login', views.login_request, name='login_url'),
    path('logout', views.logout_request, name='logout_url'),
]

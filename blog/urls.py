from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_blogs, name='home-blogs'),
]
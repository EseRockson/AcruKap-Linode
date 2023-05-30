from django.urls import path 
from .import views

urlpartterns = [
    path('', views.simple_view)

]


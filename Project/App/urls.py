from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('kids/', views.kids, name='kids'),
    path('tailors/', views.tailors, name='tailors'),
    path('team/', views.team, name='team'),
    path('login/', views.login, name='login'),
]

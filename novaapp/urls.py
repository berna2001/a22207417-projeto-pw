# novaapp/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('inicio/', views.inicio_view, name='inicio'),
    path('servicos/', views.servicos_view, name='servicos'),
    path('sobre/', views.sobre_view, name='sobre'),
]
# pwsite/urls.py

from django.urls import path
from . import views

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('index1/', views.index_view1, name='index1'),
    path('index2/', views.index_view2, name='index2'),
]
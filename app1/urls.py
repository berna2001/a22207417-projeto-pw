from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'app1'

urlpatterns = [
    path('listabandas/', views.index_view, name='listabandas'),
    path('banda/', views.index_view1, name='banda'),
    path('album/', views.index_view2, name='album'),
    path('musica/', views.index_view2, name='musica'),
]
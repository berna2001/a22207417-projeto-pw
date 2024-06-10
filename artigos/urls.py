from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.autores_view, name='lista_autores'),
    path('autor/<int:autor_id>/', views.autor_view, name='detalhes_autor'),
    path('receita/<int:artigo_receita_id>/', views.artigo_receita_view, name='detalhes_artigo_receita'),
    path('autor/novo/', views.novo_autor_view, name='novo_autor'),
    path('autor/editar/<int:autor_id>/', views.editar_autor_view, name='editar_autor'),
    path('artigo_receita/novo/', views.novo_artigo_receita_view, name='novo_artigo_receita'),
    path('artigo_receita/editar/<int:artigo_receita_id>/', views.editar_artigo_receita_view, name='editar_artigo_receita'),
]

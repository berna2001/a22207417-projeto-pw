from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.bandas_view, name='lista_bandas'),
    path('banda/<int:banda_id>/', views.banda_view, name='detalhes_banda'),
    path('album/<int:album_id>/', views.album_view, name='detalhes_album'),
    path('musica/<int:musica_id>/', views.musica_view, name='detalhes_musica'),
    path('banda/nova/', views.nova_banda_view, name='nova_banda'),
    path('banda/editar/<int:banda_id>/', views.editar_banda_view, name='editar_banda'),
    path('album/novo/', views.novo_album_view, name='novo_album'),
    path('album/editar/<int:album_id>/', views.editar_album_view, name='editar_album'),
    path('musica/nova/', views.nova_musica_view, name='nova_musica'),
    path('musica/editar/<int:musica_id>/', views.editar_musica_view, name='editar_musica'),
]

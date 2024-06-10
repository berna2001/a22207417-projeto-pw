from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.cursos_view, name='lista_cursos'),
    path('curso/<int:curso_id>/', views.curso_view, name='detalhes_curso'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='detalhes_disciplina'),
    path('projeto/<int:projeto_id>/', views.projeto_view, name='detalhes_projeto'),
    path('curso/novo/', views.novo_curso_view, name='novo_curso'),
    path('curso/editar/<int:curso_id>/', views.editar_curso_view, name='editar_curso'),
    path('disciplina/nova/', views.nova_disciplina_view, name='nova_disciplina'),
    path('disciplina/editar/<int:disciplina_id>/', views.editar_disciplina_view, name='editar_disciplina'),
]

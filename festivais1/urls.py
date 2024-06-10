from django.urls import path
from . import views

urlpatterns = [
    path('festivais1/', views.festivais_view, name='festivais1'),
    path('festivais1/<int:festival_id>/', views.festival_view, name='detalhes_festival'),
]
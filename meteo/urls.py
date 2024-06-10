from django.urls import path
from .views import lista_cidade, tempo_hoje, tempo_cinco_dias, previsao_view

app_name = 'meteo'

urlpatterns = [
    path('cities/', lista_cidade, name='lista_cidade'),
    path('weather/today/<int:city_id>/', tempo_hoje, name='tempo_hoje'),
    path('weather/five_days/<int:city_id>/', tempo_cinco_dias, name='tempo_cinco_dias'),
    path('', previsao_view, name='previsao'),
]

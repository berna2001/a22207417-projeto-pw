from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', views.index, name='index'),
    path('', views.landing_page, name='landing_page'),
    path('mebyme/', views.me_by_me, name='me_by_me'),
    path('webcheats/', views.web_cheats, name='web_cheats'),
]

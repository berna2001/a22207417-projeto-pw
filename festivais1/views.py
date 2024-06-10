from django.shortcuts import render
from .models import Festival

def festivais_view(request):
    localizacoes = Festival.objects.all()
    return render(request, 'festivais/festivais.html', {'localizacoes': localizacoes})

def festival_view(request, festival_id):
    festival = Festival.objects.get(pk=festival_id)
    return render(request, 'festivais/festival.html', {'festival': festival})
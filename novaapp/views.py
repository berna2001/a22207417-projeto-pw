from django.shortcuts import render


def inicio_view(request):
    return render(request, "novaapp/inicio.html")

def servicos_view(request):
    return render(request, "novaapp/servicos.html")

def sobre_view(request):
    return render(request, "novaapp/sobre.html")

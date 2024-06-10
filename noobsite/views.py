from django.shortcuts import render

# noobsite/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")


def index_view1(request):
    return HttpResponse("Olá, ao maior de Portugal!")

def index_view2(request):
    return HttpResponse("Olá.")

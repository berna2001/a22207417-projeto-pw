
from django.shortcuts import render

def index_view(request):
    return render(request, "app1/listabandas.html")

def index_view1(request):
    return render(request, "app1/listabandas.html")

def index_view2(request, album_id):
    return render(request, "app1/listabandas.html")

def index_view3(request):
    return render(request, "app1/listabandas.html")
from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')


def landing_page(request):
    return render(request, 'portfolio/landing_page.html')


def me_by_me(request):
    return render(request, 'portfolio/me_by_me.html')


def web_cheats(request):
    return render(request, 'portfolio/web_cheats.html')
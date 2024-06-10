from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm, MusicaForm

def grupo_necessario(nome_grupo):
    def in_group(user):
        return user.groups.filter(name=nome_grupo).exists()
    return user_passes_test(in_group)

def bandas_view(request):
    bandas = Banda.objects.all()
    context = {'bandas': bandas}
    return render(request, 'bandas/bandas_list.html', context)

def banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    albuns = Album.objects.filter(banda=banda)
    context = {'banda': banda, 'albuns': albuns}
    return render(request, 'bandas/banda_detail.html', context)

def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    musicas = Musica.objects.filter(album=album)
    context = {'album': album, 'musicas': musicas}
    return render(request, 'bandas/album_detail.html', context)

def musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    context = {'musica': musica}
    return render(request, 'bandas/musica_detail.html', context)

@login_required
@grupo_necessario('editores_bandas')
def nova_banda_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_bandas')
    else:
        form = BandaForm()
    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@login_required
@grupo_necessario('editores_bandas')
def editar_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:detalhes_banda', banda_id=banda_id)
    else:
        form = BandaForm(instance=banda)
    context = {'form': form}
    return render(request, 'bandas/editar_banda.html', context)

@login_required
@grupo_necessario('editores_bandas')
def novo_album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_bandas')
    else:
        form = AlbumForm()
    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)

@login_required
@grupo_necessario('editores_bandas')
def editar_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:detalhes_album', album_id=album_id)
    else:
        form = AlbumForm(instance=album)
    context = {'form': form}
    return render(request, 'bandas/editar_album.html', context)

@login_required
@grupo_necessario('editores_bandas')
def nova_musica_view(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_bandas')
    else:
        form = MusicaForm()
    context = {'form': form}
    return render(request, 'bandas/nova_musica.html', context)

@login_required
@grupo_necessario('editores_bandas')
def editar_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:detalhes_musica', musica_id=musica_id)
    else:
        form = MusicaForm(instance=musica)
    context = {'form': form}
    return render(request, 'bandas/editar_musica.html', context)

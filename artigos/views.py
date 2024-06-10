from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Autor, ArtigoReceita
from .forms import AutorForm, ArtigoReceitaForm

def grupo_necessario(nome_grupo):
    def in_group(user):
        return user.groups.filter(name=nome_grupo).exists()
    return user_passes_test(in_group)

def autores_view(request):
    autores = Autor.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'artigos/autores_list.html', context)

def autor_view(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    receitas = ArtigoReceita.objects.filter(autor=autor)
    context = {
        'autor': autor,
        'receitas': receitas
    }
    return render(request, 'artigos/autor_detail.html', context)

def artigo_receita_view(request, artigo_receita_id):
    artigo_receita = get_object_or_404(ArtigoReceita, id=artigo_receita_id)
    context = {
        'artigo_receita': artigo_receita
    }
    return render(request, 'artigos/artigo_receita_detail.html', context)


@login_required
@grupo_necessario('editores_artigos')
def novo_autor_view(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_autor')
    else:
        form = AutorForm()
    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)

@login_required
@grupo_necessario('editores_artigos')
def editar_autor_view(request, autor_id):
    autor= Autor.objects.get(id=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_autor', autor_id=autor_id)
    else:
        form = AutorForm(instance=autor)
    context = {'form': form}
    return render(request, 'artigos/editar_autor.html', context)


@login_required
@grupo_necessario('editores_artigos')
def novo_artigo_receita_view(request):
    if request.method == 'POST':
        form = ArtigoReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_autores')
    else:
        form = ArtigoReceitaForm()
    context = {'form': form}
    return render(request, 'artigos/novo_artigo_receita.html', context)


@login_required
@grupo_necessario('editores_artigos')
def editar_artigo_receita_view(request, artigo_receita_id):
    artigo_receita = ArtigoReceita.objects.get(id=artigo_receita_id)
    if request.method == 'POST':
        form = ArtigoReceitaForm(request.POST, instance=artigo_receita)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_artigo_receita', artigo_receita_id=artigo_receita_id)
    else:
        form = ArtigoReceitaForm(instance=artigo_receita)
    context = {'form': form}
    return render(request, 'artigos/editar_artigo_receita.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso, Disciplina, Projeto
from .forms import CursoForm, DisciplinaForm, ProjetoForm


def grupo_necessario(nome_grupo):
    def in_group(user):
        return user.groups.filter(name=nome_grupo).exists()
    return user_passes_test(in_group)

def cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/cursos_list.html', {'cursos': cursos})

def curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    disciplinas = Disciplina.objects.filter(area_cientifica__curso=curso)
    context = {
        'curso': curso,
        'disciplinas': disciplinas
    }
    return render(request, 'curso/curso_detail.html', context)

def disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    context = {
        'disciplina': disciplina
    }
    return render(request, 'curso/disciplina_detail.html', context)

def projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    context = {
        'projeto': projeto
    }
    return render(request, 'curso/projeto_detail.html', context)

@login_required
@grupo_necessario('editores_curso')
def novo_curso_view(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:lista_cursos')
    else:
        form = CursoForm()
    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)


@login_required
@grupo_necessario('editores_curso')
def editar_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_curso', curso_id=curso_id)
    else:
        form = CursoForm(instance=curso)
    context = {'form': form}
    return render(request, 'curso/editar_curso.html', context)


@login_required
@grupo_necessario('editores_curso')
def nova_disciplina_view(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_curso')
    else:
        form = DisciplinaForm()
    context = {'form': form}
    return render(request, 'curso/nova_disciplina.html', context)

@login_required
@grupo_necessario('editores_curso')
def editar_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_disciplina', disciplina_id=disciplina_id)
    else:
        form = DisciplinaForm(instance=disciplina)
    context = {'form': form}
    return render(request, 'curso/editar_disciplina.html', context)


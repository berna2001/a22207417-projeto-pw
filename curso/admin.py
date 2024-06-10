from django.contrib import admin
from .models import Curso, Docente, LinguagemProgramacao, AreaCientifica, Disciplina, Projeto

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(LinguagemProgramacao)
class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(AreaCientifica)
class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'curricular_unit_readable_code', 'area_cientifica')
    filter_horizontal = ('docentes',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'ano', 'semestre', 'descricao')

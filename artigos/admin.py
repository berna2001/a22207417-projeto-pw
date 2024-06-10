from django.contrib import admin

from .models import Autor
from .models import ArtigoReceita


admin.site.register(Autor)

class ArtigoReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'tempo_preparo')
    search_fields = ['titulo', 'autor__nome']

admin.site.register(ArtigoReceita, ArtigoReceitaAdmin)

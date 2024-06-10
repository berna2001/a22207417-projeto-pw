from django.contrib import admin
from .models import Banda, Album, Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_formacao')
    search_fields = ('nome',)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'banda', 'ano_lancamento')
    list_filter = ('banda', 'ano_lancamento')
    search_fields = ('titulo', 'banda__nome')

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracao')
    list_filter = ('album__banda', 'album')
    search_fields = ('titulo', 'album__titulo')

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)

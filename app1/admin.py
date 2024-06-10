from django.contrib import admin

# Register your models here.

from .models import Banda
from .models import Album
from .models import Musica

class MusicaInline(admin.TabularInline):
    model = Musica

class AlbumAdmin(admin.ModelAdmin):
    inlines = [MusicaInline]

admin.site.register(Banda)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica)
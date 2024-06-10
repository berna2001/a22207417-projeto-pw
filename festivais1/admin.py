from django.contrib import admin
from .models import Banda, Festival, Localizacao


admin.site.register(Localizacao)
admin.site.register(Banda)
admin.site.register(Festival)

# loader.py

from bandas.models import Banda, Album, Musica
import json

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)

    for banda in bandas['bandas']:
        Banda.objects.create(
            nome=banda['nome'],
            nacionalidade=banda['nacionalidade'],
            ano_formacao=banda['ano_formacao']
        )

with open('bandas/json/discos.json') as f:
    discos = json.load(f)

    for disco in discos['discos']:
        banda = Banda.objects.get(nome=disco['banda'])
        album = Album.objects.create(
            titulo=disco['titulo'],
            ano_lancamento=disco['ano_lancamento'],
            banda=banda
        )

        for musica in disco['musicas']:
            Musica.objects.create(
                titulo=musica['titulo'],
                duracao=musica['duracao'],
                album=album
            )

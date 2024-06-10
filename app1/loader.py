import json
from .models import Banda, Album, Musica

Banda.objects.all().delete()
Album.objects.all().delete()


with open('app1/json/bandas.json') as f:
    bandas_data = json.load(f)
    for banda_key, banda_data in bandas_data.items():
        Banda.objects.create(
            nome=banda_data['nome'],
            nacionalidade=banda_data['nacionalidade'],
            ano_criacao=banda_data['ano_criacao'],
        )

# Load albuns.json
with open('app1/json/albuns.json') as f:
    albuns_data = json.load(f)
    for album_key, album_data in albuns_data.items():
        banda = Banda.objects.get(nome=album_data['banda'])
        album = Album.objects.create(
            banda=banda,
            titulo=album_data['titulo'],
            ano_lancamento=album_data['ano_lancamento']
        )
        for musica_data in album_data['musicas'].items():
            Musica.objects.create(
                album=album,
                titulo=musica_data[0],
                duracao=musica_data[1]
            )
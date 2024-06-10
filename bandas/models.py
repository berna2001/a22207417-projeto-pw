from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100, default="Desconhecido")
    ano_formacao = models.IntegerField()

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, related_name='albuns', on_delete=models.CASCADE)
    ano_lancamento = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='album_capas/', blank=True)

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duracao = models.CharField(max_length=100)
    link_spotify = models.URLField(blank=True)

    def __str__(self):
        return self.titulo


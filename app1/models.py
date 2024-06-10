from django.db import models



class Banda(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='bandas/')
    informacoes = models.TextField()
    nacionalidade = models.CharField(max_length=50)
    ano_criacao = models.IntegerField()

    def __str__(self):
        return self.nome


class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    capa = models.ImageField(upload_to='albums/')
    ano_lancamento = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.banda})"

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    spotify_link = models.URLField(blank=True, null=True)
    duracao = models.DurationField()

    def __str__(self):
        return f"{self.titulo} ({self.album})"
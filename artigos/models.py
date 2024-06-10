from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nome

class ArtigoReceita(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    ingredientes = models.TextField()
    tempo_preparo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='receitas/')

    def __str__(self):
        return self.titulo
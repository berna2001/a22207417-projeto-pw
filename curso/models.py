from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return self.titulo

class Docente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, related_name='areas_cientificas', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=25)
    docentes = models.ManyToManyField(Docente)
    ects = models.IntegerField()
    curricular_unit_readable_code = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=25)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    linguagens_programacao = models.ManyToManyField(LinguagemProgramacao)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    video_demo = models.URLField()
    link_github = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Projeto de {self.disciplina.nome} ({self.ano}/{self.semestre})"






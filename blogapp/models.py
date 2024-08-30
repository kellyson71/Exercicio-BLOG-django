from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_conclusao = models.DateField()

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='projetos/')
    resumo = models.TextField()

    def __str__(self):
        return self.titulo

from django.db import models

# Create your models here.

class categoria(models.Model):
    nome = models.CharField(max_length=20)

class Postagem(models.Model):
    titulo = models.CharField(max_length=180)
    conteudo = models.TextField()
    criador_em = models.DateTimeField(auto_now_add=True)
    ultima_modificacão = models.DateTimeField(auto_now=True)
    categoria = models.ManyToManyField('categoria', related_name='postagens')

class Comentario(models.Model):
    autor = models.CharField(max_length=60)
    corpo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE),

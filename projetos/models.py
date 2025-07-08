# projetos/models.py

from django.db import models

class Projeto(models.Model):  # Nome da classe corrigido com P maiúsculo e singular
    titulo = models.CharField(verbose_name='Título',max_length=200)
    descricao = models.TextField(verbose_name='Descrição')
    tecnologia = models.CharField(verbose_name='tecnologia', max_length=100)
    imagem = models.ImageField(verbose_name='imagem', upload_to='imagem_progetos')
    publicado = models.BooleanField(verbose_name='publicado', default=True)

    def __str__(self):
        return self.titulo.title()

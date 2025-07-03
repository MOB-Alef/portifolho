# projetos/models.py

from django.db import models

class Projeto(models.Model):  # Nome da classe corrigido com P maiúsculo e singular
    titulo = models.CharField(verbose_name='Título',max_length=200)
    descricao = models.TextField(verbose_name='Descrição')
    tecnologia = models.CharField(max_length=100)
    imagem = models.ImageField(
        upload_to='imagens_projetos/',
        blank=True,
        null=True,
        default='imagens_projetos/padrao.png'
    )

    def __str__(self):
        return self.titulo

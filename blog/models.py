from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    titulo = models.CharField(max_length=180, verbose_name='Título')
    conteudo = models.TextField(verbose_name='Conteúdo')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    ultima_modificacao = models.DateTimeField(auto_now=True, verbose_name='Última modificação')
    categorias = models.ManyToManyField(Categoria, related_name='postagens', verbose_name='Categorias')

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.CharField(max_length=60, verbose_name='Autor')
    corpo = models.TextField(verbose_name='Comentário')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios', verbose_name='Postagem')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return f'Comentário de {self.autor} em "{self.postagem}"'

# blog/models.py
postagem = models.ForeignKey(
    'Postagem',
    on_delete=models.CASCADE,
    related_name='comentarios',
    verbose_name='Postagem',
    null=True,  # Permite nulo temporariamente
    blank=True
)
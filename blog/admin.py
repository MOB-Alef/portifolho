from django.contrib import admin
from .models import Postagem

admin.site.register(Postagem)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao', 'publicado')
    list_filter = ('autor', 'data_publicacao', 'publicado')
    search_fields = ('titulo', 'conteudo')
    ordering = ('-data_publicacao',)


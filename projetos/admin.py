from django.contrib import admin
from .models import Projeto

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo_upper', 'tecnologia', 'descricao')
    list_filter = ('tecnologia',)
    ordering = ('tecnologia',)
    search_fields = ('titulo',)

    @admin.display(description='Título')
    def titulo_upper(self, obj):
        return obj.titulo.upper()

admin.site.register(Projeto, ProjetoAdmin)

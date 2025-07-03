from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='projetos_index'),
    path('<int:pk>/', views.detalhe, name='projetos_detalhe'),
    path('novo/', views.criar, name='projetos_criar'),           # Novo projeto
    path('<int:pk>/editar/', views.editar, name='projetos_editar'), # Editar projeto
    path('<int:pk>/deletar/', views.deletar, name='projetos_deletar'), # Deletar projeto
]
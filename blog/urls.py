# blog/urls.py
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path( 'postagem/<int:pk>/', views.blog_detalhe, name='blog_detalhe'),
    path('categoria/<str:categoria>/', views.blog_detalhe, name='blog_categoria'),

]
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.get_funcionarios, name='get_funcionarios'),
    path('nome/<str:nome>', views.get_by_nome, name='get_funcionarios_by_name'),
    path('add', views.cria_funcionario, name='cria_funcionario'),
    path('update', views.atualiza_funcionario, name='atualiza_funcionario'),
    path('delete', views.delete_funcionario, name='delete_funcionario')
]
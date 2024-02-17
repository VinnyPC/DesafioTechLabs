from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_funcionarios, name='get_funcionarios'),
    path('nome/<str:nome>', views.get_by_nome, name=''),
    path('data/', views.gerencia_funcionario, name='gerencia_funcionario')
]
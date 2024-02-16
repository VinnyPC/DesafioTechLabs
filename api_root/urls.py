from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('api_funcionarios.urls'), name='funcionarios_urls'),
]

from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Registro de funcionários",
        default_version='v1',
        description="API que permita consultar, registrar, atualizar e deletar funcionários",
        contact=openapi.Contact(email="viniciusdasilvadev@gmail.com"),
        extra={"repository": "https://github.com/VinnyPC/DesafioTechLabs"},
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('api_funcionarios.urls'), name='funcionarios_urls'),
    path('playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

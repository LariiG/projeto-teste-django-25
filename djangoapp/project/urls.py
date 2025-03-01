
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index_view

urlpatterns = [
        path('', index_view, name='index'),  # Adicionando a URL para a página inicial
        path('admin/', admin.site.urls),     # Página de administração
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Para servir arquivos estáticos (se necessário)

#if settings.DEBUG:
 #   urlpatterns += static(
  #      settings.MEDIA_URL,
   #     document_root=settings.MEDIA_ROOT
    #)
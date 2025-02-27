from django.contrib import admin
from django.urls import path, include  # Incluindo a função 'include' para incluir as URLs da aplicação

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoapp.projetc.urls')),  # Incluindo as URLs da aplicação projetc
]

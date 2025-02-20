# gestion_taches/urls.py
from django.contrib import admin
from django.urls import path, include
from gestion.views import home  # Importez la vue home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Ajoutez cette ligne pour la page d'accueil
    path('gestion/', include('gestion.urls')),
]
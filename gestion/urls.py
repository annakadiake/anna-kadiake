# gestion/urls.py
from django.urls import path
from .views import register, profile_update, project_create, project_list, project_update, project_delete, login_view,project_detail


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/update/', profile_update, name='profile_update'),
    path('projects/create/', project_create, name='project_create'),
    path('projects/', project_list, name='project_list'),
    path('projects/update/<int:pk>/', project_update, name='project_update'),
    path('projects/delete/<int:pk>/', project_delete, name='project_delete'),
    path('login/', login_view, name='login'),
    path('projects/<int:project_id>/', project_detail, name='project_detail'),  # Ajoutez cette ligne# Assurez-vous que cette ligne est présente
]
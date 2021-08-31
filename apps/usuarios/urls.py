from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_externos/', views.cadastro_externos, name='cadastro_externos'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/<int:id>', views.dashboard, name='dashboard'),
    path('dashboard/perfil/<int:id>', views.perfil, name='perfil'),
]

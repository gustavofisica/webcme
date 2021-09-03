from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_docente/', views.cadastro_docente, name='cadastro_docente'),
    path('cadastro_externos/', views.cadastro_externos, name='cadastro_externos'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('ativar_usuario/', views.ativar_usuario, name='ativar_usuario'),
    path('<int:id>/dashboard/', views.dashboard, name='dashboard'),
    path('<int:id>/dashboard/perfil/', views.perfil, name='perfil'),
    path('<int:id>/dashboard/alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('<int:id>dashboard/equipamento/', views.cria_equipamento, name='cria_equipamento'),
]

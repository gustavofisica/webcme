from django.urls import path
from . import views

urlpatterns = [
    # URLs de Cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_docente/<int:consultado_no_SIGA>', views.cadastro_docente, name='cadastro_docente'),
    path('cadastro_discente/<int:consultado_no_SIGA>', views.cadastro_discente, name='cadastro_discente'),
    path('cadastro_externos/', views.cadastro_externos, name='cadastro_externos'),
    # URLs de Login
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('ativar_usuario/<usuario_id64>/<token>', views.ativar_usuario, name='ativar_usuario'),
    # URLs do Dashboard
    path('<str:username>/dashboard/', views.dashboard, name='dashboard'),
    path('<str:username>/dashboard/perfil/', views.perfil, name='perfil'),
    path('<str:username>/dashboard/alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('<str:username>/dashboard/equipamento/', views.cria_equipamento, name='cria_equipamento'),
]

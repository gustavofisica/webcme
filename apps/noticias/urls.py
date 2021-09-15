from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.noticia, name='noticia'),
    path('categoria/<str:categoria>', views.lista_noticias, name='lista_noticias'),
    path('<str:username>/dashboard/nova_noticia', views.nova_noticia, name='nova_noticia'),
]
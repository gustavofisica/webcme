from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastro_externos', views.cadastro_externos, name='cadastro_externos'),
]

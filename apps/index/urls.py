from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sistema_de_gerenciamento', views.sistema_gerenciamento,
         name='sistema_gerenciamento'),
    path('normas', views.normas, name='normas'),
]

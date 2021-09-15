from noticias.models import Noticia
from django import forms
from django.forms import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from tempus_dominus.widgets import DatePicker

class FormularioNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        exclude = ['slug', 'autor']
        labels = {
            'titulo': 'Título da Notícia',
            'texto': 'Texto',
            'criacao': 'Data de Criação',
            'edicao': 'Data de Edição',
            'status': 'Marque para publicar',
            'destaque': 'Destacar notícia',
            'categoria': 'Categoria',
        }
        widgets = {
            'criacao': DatePicker(),
            'edicao': DatePicker(),
            'texto': SummernoteWidget (),
        }

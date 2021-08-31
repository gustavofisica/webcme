from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import fields
from django.forms import widgets


from .models import Usuario, Docente


class UsuarioFormularioCriacao(UserCreationForm):
    """Formulário de criação de usuário padrão"""

    class Meta(UserCreationForm.Meta):
        model = Usuario


class UsuarioFormularioModificacao(UserChangeForm):
    """Formulário de edição de usuário padrão"""

    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ('foto_de_perfil', 'username',
                  'email', 'first_name', 'last_name', 'curriculo_lattes', )
        

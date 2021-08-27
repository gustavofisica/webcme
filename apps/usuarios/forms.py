from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.core.validators import URLValidator
import uuid

from .models import Usuario, Docente

class UsuarioFormularioCriacao(UserCreationForm):
    """Formulário de criação de usuário padrão"""

    class Meta(UserCreationForm.Meta):
        model = Usuario


class UsuarioFormularioModificacao(UserChangeForm):
    """Formulário de edição de usuário padrão"""

    class Meta(UserChangeForm.Meta):
        model = Usuario

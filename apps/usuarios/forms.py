from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


class UsuarioFormularioCriacao(UserCreationForm):
    """Formulário de criação de usuário padrão"""

    class Meta(UserCreationForm.Meta):
        model = Usuario


class UsuarioFormularioModificacao(UserChangeForm):
    """Formulário de edição de usuário padrão"""

    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ('foto_de_perfil', 'email', 'first_name',
                  'last_name', 'curriculo_lattes', 'password',)

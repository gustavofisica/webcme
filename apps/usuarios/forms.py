from django import forms
from django.forms.fields import EmailField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from usuarios.models import Usuario
from usuarios.validation import *
import uuid


class UsuarioFormularioCriacao(UserCreationForm):
    """Formulário de criação de usuário padrão"""
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput)
    email1 = forms.EmailField(label='E-mail')
    email2 = forms.EmailField(
        label='Confirmação de e-mail')

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("email",)
        field_classes = {'email': EmailField}

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username is None:
            username = uuid.uuid4()

    def clean_email2(self):
        # Check that the two email entries match
        email1 = self.cleaned_data.get("email1")
        email2 = self.cleaned_data.get("email2")
        if email1 and email2 and email1 != email2:
            raise ValidationError("Emails não correspondem")
        elif Usuario.objects.filter(email=email2).exists():
            raise ValidationError("Usuário já cadastrado")
        return email2

    def save(self, commit=True):
        # Save the provided password in hashed format
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class UsuarioFormularioModificacao(UserChangeForm):
    """Formulário de edição de usuário padrão"""

    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ('foto_de_perfil', 'email', 'first_name',
                  'last_name', 'curriculo_lattes', 'password',)

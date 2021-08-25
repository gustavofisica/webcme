from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.db import models

from .forms import UserChangeForm, UserCreationForm
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('foto_de_perfil',)}),
    )

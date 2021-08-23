from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Equipamento

# Register your models here.
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_do_equipamento',)

admin.site.register(Equipamento, EquipamentoAdmin)

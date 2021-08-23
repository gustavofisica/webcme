from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Equipamento, GeleriaEquipamento

# Register your models here.
class ImagemInline(admin.TabularInline):
    model = GeleriaEquipamento

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    inlines = [
        ImagemInline
    ]

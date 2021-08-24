# Generated by Django 3.2.6 on 2021-08-24 18:53

from django.db import migrations, models
import django.db.models.deletion
import equipamentos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_equipamento', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GeleriaEquipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to=equipamentos.models.nomear_pasta)),
                ('descricao_da_imagem', models.CharField(max_length=500)),
                ('foto_de_perfil', models.BooleanField(default=False)),
                ('miniatura', models.ImageField(editable=False, upload_to=equipamentos.models.nomear_pasta)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='equipamentos.equipamento')),
            ],
        ),
    ]

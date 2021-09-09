# Generated by Django 3.2.6 on 2021-09-09 00:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_alter_usuario_caminho_armazenamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='caminho_armazenamento',
            field=models.UUIDField(default=uuid.UUID('b3f3f5eb-67de-42a0-ad31-d5edc982d72c'), editable=False),
        ),
        migrations.CreateModel(
            name='Discente',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
                ('vinculo', models.CharField(blank=True, max_length=25, null=True)),
                ('inicio_vinculo', models.DateField()),
                ('setor', models.CharField(blank=True, max_length=25, null=True)),
                ('departamento', models.CharField(blank=True, max_length=25, null=True)),
                ('periodo_de_permanencia', models.DateField()),
                ('docente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.docente')),
            ],
        ),
    ]
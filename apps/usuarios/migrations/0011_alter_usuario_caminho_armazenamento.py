# Generated by Django 3.2.6 on 2021-09-03 00:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_usuario_caminho_armazenamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='caminho_armazenamento',
            field=models.UUIDField(default=uuid.UUID('5250b9cd-3d37-4824-ab5f-b0df03d77075'), editable=False),
        ),
    ]
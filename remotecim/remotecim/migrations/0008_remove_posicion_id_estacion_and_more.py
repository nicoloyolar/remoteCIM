# Generated by Django 4.1.8 on 2023-07-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remotecim', '0007_usuario_horario_confirmado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posicion',
            name='id_estacion',
        ),
        migrations.RemoveField(
            model_name='posicion',
            name='id_posicion',
        ),
        migrations.AddField(
            model_name='posicion',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

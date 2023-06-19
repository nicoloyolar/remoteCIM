# Generated by Django 4.1.8 on 2023-06-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remotecim', '0005_alter_estaciondetrabajo_disponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ultima_estacion',
            field=models.CharField(blank=True, choices=[('almacenamiento', 'Almacenamiento'), ('mecanizado', 'Mecanizado'), ('control_de_calidad', 'Control de Calidad')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='estaciondetrabajo',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
    ]

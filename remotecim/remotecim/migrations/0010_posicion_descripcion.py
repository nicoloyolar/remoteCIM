# Generated by Django 5.0.1 on 2024-02-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remotecim', '0009_remove_posicion_coordenadas_posicion_coordenada_p_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posicion',
            name='descripcion',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.8 on 2023-07-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remotecim', '0006_usuario_ultima_estacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='horario_confirmado',
            field=models.BooleanField(default=False),
        ),
    ]

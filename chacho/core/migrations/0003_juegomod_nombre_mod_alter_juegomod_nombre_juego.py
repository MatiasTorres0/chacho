# Generated by Django 5.0.1 on 2024-01-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_juegomod_delete_juegomodform'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegomod',
            name='nombre_mod',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='juegomod',
            name='nombre_juego',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_juegomod_nombre_mod_alter_juegomod_nombre_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegomod',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('realizado', 'Realizado')], default='pendiente', max_length=20),
        ),
    ]
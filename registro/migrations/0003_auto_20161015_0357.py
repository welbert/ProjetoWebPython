# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161015062527 on 2016-10-15 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_militar_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cautela_Militar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='militar',
            options={'verbose_name_plural': 'Militares'},
        ),
        migrations.AlterModelOptions(
            name='municao',
            options={'verbose_name_plural': 'Municoes'},
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'verbose_name': 'Reservas de Material', 'verbose_name_plural': 'Reservas de Materiais'},
        ),
        migrations.AddField(
            model_name='cautela_militar',
            name='militar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='militar', to='registro.Militar'),
        ),
        migrations.AddField(
            model_name='cautela_militar',
            name='militar_resp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='militar_resp', to='registro.Militar'),
        ),
    ]

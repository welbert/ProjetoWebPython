# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161011220334 on 2016-10-11 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20161011_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='acessorio',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='armamento',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='municao',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161021143717 on 2016-10-21 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_auto_20161021_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cautela_acessorio',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='cautela_municao',
            options={'managed': False},
        ),
    ]

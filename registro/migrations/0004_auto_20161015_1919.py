# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161015071413 on 2016-10-15 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20161015_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cautela_armamento',
            name='data_de_retirada',
            field=models.CharField(max_length=20, verbose_name=b'Data de Retirada'),
        ),
    ]

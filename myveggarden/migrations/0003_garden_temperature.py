# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-06-07 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myveggarden', '0002_auto_20180601_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='temperature',
            field=models.CharField(default='', max_length=140),
        ),
    ]

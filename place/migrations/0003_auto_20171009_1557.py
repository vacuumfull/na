# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20171009_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['address'], 'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
    ]

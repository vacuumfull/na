# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20171009_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bands',
            field=models.ManyToManyField(blank=True, null=True, related_name='event_bands', to='band.Band', verbose_name='Команды'),
        ),
    ]
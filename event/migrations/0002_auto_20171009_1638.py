# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 13:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_auto_20171009_1638'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('band', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='bands',
            field=models.ManyToManyField(blank=True, null=True, to='band.Band', verbose_name='Команды'),
        ),
        migrations.AddField(
            model_name='event',
            name='locations',
            field=models.ManyToManyField(related_name='event_location', to='place.Location', verbose_name='Место проведения'),
        ),
        migrations.AddField(
            model_name='event',
            name='musicians',
            field=models.ManyToManyField(blank=True, null=True, related_name='event_musicians', to=settings.AUTH_USER_MODEL, verbose_name='Музыканты'),
        ),
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_owner', to=settings.AUTH_USER_MODEL, verbose_name='Организатор'),
        ),
    ]
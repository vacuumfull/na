# Generated by Django 2.0 on 2018-01-12 20:19

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('event', '0008_auto_20180112_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='event_tags', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Тэги'),
        ),
    ]

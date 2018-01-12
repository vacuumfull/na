# Generated by Django 2.0 on 2018-01-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20171102_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='locations',
            field=models.ManyToManyField(related_name='event_location', to='place.Place', verbose_name='Место проведения'),
        ),
    ]

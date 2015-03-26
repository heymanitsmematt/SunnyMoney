# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Precipitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeatherDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('hail', models.BooleanField()),
                ('snow', models.BooleanField()),
                ('fog', models.BooleanField()),
                ('rain', models.BooleanField()),
                ('minTemp', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('meanTemp', models.IntegerField()),
                ('minHumidity', models.IntegerField()),
                ('maxHumidity', models.IntegerField()),
                ('precipitation', models.IntegerField()),
                ('snowfall', models.IntegerField()),
                ('precipsource', models.ForeignKey(to='DataScraper.Precipitation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

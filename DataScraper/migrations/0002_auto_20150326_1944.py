# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataScraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('adjClose', models.FloatField()),
                ('company', models.ForeignKey(to='DataScraper.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='weatherday',
            name='precipsource',
        ),
        migrations.DeleteModel(
            name='Precipitation',
        ),
    ]

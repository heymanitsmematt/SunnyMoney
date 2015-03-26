# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataScraper', '0002_auto_20150326_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockday',
            name='adjClose',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockday',
            name='close',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockday',
            name='high',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockday',
            name='low',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockday',
            name='open',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]

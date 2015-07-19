# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20150704_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='country',
            field=models.CharField(max_length=45, null=True, verbose_name='City', choices=[(b'ch', 'Switzerland'), (b'de', 'Germany')]),
        ),
        migrations.AddField(
            model_name='appartement',
            name='postal_code',
            field=models.CharField(max_length=45, null=True, verbose_name='Postal Code'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price (per Month'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='rooms',
            field=models.FloatField(default=0, verbose_name='Price (per Month'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='street_nr',
            field=models.CharField(max_length=255, null=True, verbose_name='Street'),
        ),
    ]

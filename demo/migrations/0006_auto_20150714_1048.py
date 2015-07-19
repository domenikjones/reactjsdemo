# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('demo', '0005_auto_20150714_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='main_image',
            field=filer.fields.image.FilerImageField(to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='appartement',
            name='country',
            field=models.CharField(max_length=45, null=True, verbose_name='Country', choices=[(b'ch', 'Switzerland'), (b'de', 'Germany')]),
        ),
        migrations.AlterField(
            model_name='appartement',
            name='rooms',
            field=models.FloatField(default=0, verbose_name='Rooms'),
        ),
    ]

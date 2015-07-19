# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_auto_20150715_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='price_netto',
            field=models.IntegerField(default=0, verbose_name='Price Netto (per Month'),
        ),
    ]

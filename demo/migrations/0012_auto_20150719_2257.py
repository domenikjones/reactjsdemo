# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_auto_20150719_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appartementimage',
            options={'ordering': ('priority',), 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AddField(
            model_name='appartementimage',
            name='priority',
            field=models.SmallIntegerField(default=0, verbose_name='Priority'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20150704_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='publish_date_end',
            field=models.DateTimeField(null=True, verbose_name='End Date', blank=True),
        ),
        migrations.AddField(
            model_name='appartement',
            name='publish_date_start',
            field=models.DateTimeField(null=True, verbose_name='Start Date', blank=True),
        ),
        migrations.AddField(
            model_name='appartement',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='appartement',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(editable=False, blank=True),
        ),
    ]

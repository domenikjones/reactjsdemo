# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150704_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='appartement',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True),
        ),
    ]

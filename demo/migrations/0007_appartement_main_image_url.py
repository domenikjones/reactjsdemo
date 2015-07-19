# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20150714_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='main_image_url',
            field=models.URLField(null=True, verbose_name='Main Image URL'),
        ),
    ]

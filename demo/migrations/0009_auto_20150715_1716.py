# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_auto_20150715_1714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppartementTyp',
            new_name='AppartementType',
        ),
    ]

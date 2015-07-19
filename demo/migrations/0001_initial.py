# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Created', auto_created=True)),
                ('created', models.DateTimeField(verbose_name='Created', auto_created=True)),
                ('uuid', models.UUIDField()),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('title', models.CharField(max_length=45, verbose_name='Title')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Appartement',
                'verbose_name_plural': 'Appartements',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import filer.fields.image
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('demo', '0010_appartement_price_netto'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppartementImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='appartement',
            name='country',
            field=models.CharField(max_length=45, null=True, verbose_name='Country', choices=[(b'ch', 'Switzerland'), (b'de', 'Germany'), (b'us', 'United States of America')]),
        ),
        migrations.AlterField(
            model_name='appartement',
            name='types',
            field=models.ManyToManyField(related_name='appartement_types', null=True, to='demo.AppartementType'),
        ),
        migrations.AddField(
            model_name='appartementimage',
            name='appartement',
            field=models.ForeignKey(related_name='appartement_images', to='demo.Appartement'),
        ),
        migrations.AddField(
            model_name='appartementimage',
            name='image',
            field=filer.fields.image.FilerImageField(to='filer.Image'),
        ),
    ]

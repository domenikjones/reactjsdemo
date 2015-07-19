# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import filer.fields.image
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_appartement_main_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppartementTyp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='Type')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Appartement Type',
                'verbose_name_plural': 'Appartement Types',
            },
        ),
        migrations.AddField(
            model_name='appartement',
            name='available',
            field=models.DateField(null=True, verbose_name='Available Date'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='balconies',
            field=models.SmallIntegerField(default=0, verbose_name='Balconies'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='balconies_space',
            field=models.SmallIntegerField(default=0, verbose_name='Balconies Space'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='contact_email',
            field=models.CharField(max_length=255, null=True, verbose_name='Contact Email'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='contact_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Contact Name'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='contact_phone',
            field=models.CharField(max_length=255, null=True, verbose_name='Contact Phone'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='floor',
            field=models.SmallIntegerField(default=1, verbose_name='Floor'),
        ),
        migrations.AddField(
            model_name='appartement',
            name='living_space',
            field=models.SmallIntegerField(default=0, verbose_name='Living Space'),
        ),
        migrations.AlterField(
            model_name='appartement',
            name='main_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='appartement',
            name='main_image_url',
            field=models.URLField(null=True, verbose_name='Main Image URL', blank=True),
        ),
        migrations.AddField(
            model_name='appartement',
            name='types',
            field=models.ManyToManyField(to='demo.AppartementTyp', null=True),
        ),
    ]

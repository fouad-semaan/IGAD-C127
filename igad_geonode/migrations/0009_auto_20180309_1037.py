# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0008_auto_20180309_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='color',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='icon',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='title',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]

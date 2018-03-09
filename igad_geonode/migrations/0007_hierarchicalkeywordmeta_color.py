# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0006_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='hierarchicalkeywordmeta',
            name='color',
            field=models.CharField(max_length=128, null=True),
        ),
    ]

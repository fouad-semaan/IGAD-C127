# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0007_hierarchicalkeywordmeta_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='icon',
            field=models.CharField(max_length=128, null=True),
        ),
    ]

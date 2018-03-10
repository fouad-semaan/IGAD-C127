# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0009_auto_20180309_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='hkeyword',
            field=models.OneToOneField(related_name='meta', to='base.HierarchicalKeyword'),
        ),
    ]

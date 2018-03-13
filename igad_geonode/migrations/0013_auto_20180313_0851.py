# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0012_hierarchicalkeywordmeta_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hierarchicalkeywordmeta',
            options={'ordering': ['order']},
        ),
    ]

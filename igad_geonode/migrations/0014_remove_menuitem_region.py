# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0013_auto_20180313_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='region',
        ),
    ]

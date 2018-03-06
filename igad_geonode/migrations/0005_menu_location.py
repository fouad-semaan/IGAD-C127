# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_auto_20171114_0341'),
        ('igad_geonode', '0004_menu_item_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='location',
            field=models.CharField(default=b'top', max_length=32, db_index=True, choices=[(b'top', 'Top menu'), (b'sidebar', 'Search sidebar')]),
        )
    ]

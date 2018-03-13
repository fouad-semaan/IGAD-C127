# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import igad_geonode.models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0011_menuitem_blank'),
    ]

    operations = [
        migrations.AddField(
            model_name='hierarchicalkeywordmeta',
            name='order',
            field=models.IntegerField(default=igad_geonode.models.get_hkeyword_meta_order, help_text='Position of category, ascending'),
        ),
    ]

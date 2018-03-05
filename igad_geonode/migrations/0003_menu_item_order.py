# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import igad_geonode.models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0002_external_links'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='menuitem',
            name='order',
            field=models.IntegerField(default=igad_geonode.models.get_menu_item_order, help_text='Position of menu item, ascending'),
        ),
    ]

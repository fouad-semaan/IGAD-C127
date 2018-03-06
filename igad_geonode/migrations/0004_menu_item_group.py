# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0027_auto_20180105_1631'),
        ('igad_geonode', '0003_menu_item_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='group',
            field=models.ForeignKey(blank=True, to='groups.GroupProfile', null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0010_auto_20180309_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='blank',
            field=models.BooleanField(default=True, help_text='Open link in new browser window', verbose_name='New window'),
        ),
    ]

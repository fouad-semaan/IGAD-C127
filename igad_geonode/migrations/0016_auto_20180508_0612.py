# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-08 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0015_auto_20180508_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hierarchicalkeywordmeta',
            name='icon',
            field=models.ImageField(default=b'img/icons/blank.png', upload_to=b'img/%Y/%m'),
        ),
    ]
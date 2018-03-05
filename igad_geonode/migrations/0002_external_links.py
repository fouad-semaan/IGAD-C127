# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import igad_geonode.models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0001_init'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=igad_geonode.models.get_menu_order, help_text=b'Position of menu, ascending')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('url', models.URLField(unique=True)),
                ('menu', models.ForeignKey(to='igad_geonode.Menu')),
            ],
        ),
    ]

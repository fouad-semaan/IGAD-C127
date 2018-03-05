# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igad_geonode', '0001_init'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu', models.CharField(default=b'external_link', max_length=32, db_index=True, choices=[(b'external_link', 'External Links')])),
                ('title', models.CharField(unique=True, max_length=255)),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]

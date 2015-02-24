# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0016_auto_20150224_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='is_part_of_series',
            field=models.BooleanField(default=False, help_text=b"If you are not sure, tick the box and select 'Unknown' below", verbose_name=b'Is or was this map part of a series?'),
            preserve_default=True,
        ),
    ]

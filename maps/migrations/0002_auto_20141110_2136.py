# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='series_indicator',
            new_name='is_part_of_series',
        ),
    ]

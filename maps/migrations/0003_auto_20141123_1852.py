# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20141123_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='disaggregated_affected_population_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=16, null=True, choices=[(b'Age', b'Age'), (b'Gender', b'Gender'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='humanitarian_profile_level_1_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=103, null=True, choices=[(b'Numbers of dead', b'Numbers of dead'), (b'Numbers of missing/injured', b'Numbers of missing/injured'), (b'Numbers of displaced', b'Numbers of displaced'), (b'Number affected but not displaced', b'Number affected but not displaced'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
    ]

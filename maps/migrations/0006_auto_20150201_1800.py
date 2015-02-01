# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_reviewgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewgroup',
            name='extent_options',
            field=models.TextField(default='Country\nAffected regions', help_text=b'Specify what should appear in the Extent dropdown (one per line).'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='map',
            name='extent',
            field=multiselectfield.db.fields.MultiSelectField(help_text=b'Geographical extent of the map.', max_length=200),
            preserve_default=True,
        ),
    ]

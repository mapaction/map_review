# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0013_auto_20150222_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewgroup',
            name='map_url_help_text',
            field=models.CharField(help_text=b'Where should the reviewer link to? (E.g. ReliefWeb)', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]

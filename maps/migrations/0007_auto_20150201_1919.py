# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import maps.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_auto_20150201_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='review_created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 19, 19, 51, 655482, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='map',
            name='extent',
            field=maps.models.ExtentMultiSelectField(help_text=b'Geographical extent of the map.', max_length=22, choices=[(b'Country', b'Country'), (b'Affected areas', b'Affected areas')]),
            preserve_default=True,
        ),
    ]

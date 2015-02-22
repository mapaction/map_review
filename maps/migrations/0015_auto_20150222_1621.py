# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0014_reviewgroup_map_url_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewgroup',
            name='admin_levels_help_text',
            field=models.TextField(help_text=b'An explanation of what e.g. Admin Level 4 means in the context of the region/country being mapped.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='admin_max_detail_level',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'Level 1', b'Level 1'), (b'Level 2', b'Level 2'), (b'Level 3', b'Level 3'), (b'Level 4', b'Level 4')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='copyright',
            field=models.TextField(help_text=b"You can just enter 'Yes' instead of the copyright text if you wish. We will update this later.", null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='disclaimer',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=114, null=True, help_text=b'Type of disclaimer appearing on the map', choices=[(b'None', b'None'), (b'General disclaimer', b'General disclaimer'), (b'Narrative on possible errors/limitations', b'Narrative on possible errors/limitations'), (b'Uses statistical confidence measures for the data', b'Uses statistical confidence measures for the data')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='infographics',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=43, null=True, help_text=b'List of infographics or other non-map items appearing on the map', choices=[(b'Infographic', b'Infographic'), (b'Pie chart', b'Pie chart'), (b'Bar chart', b'Bar chart'), (b'Table', b'Table'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='is_part_of_series',
            field=models.BooleanField(default=False, help_text=b"If you are not sure, tick the box and select 'Unknown' below", verbose_name=b'Is or was this map part of a series?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='update_frequency',
            field=models.CharField(blank=True, max_length=10, null=True, help_text=b'If the map was part of a series, approximately how frequently was it updated?', choices=[(b'Unknown', b'Unknown'), (b'Daily', b'Daily'), (b'Weekly', b'Weekly'), (b'Monthly', b'Monthly'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
    ]

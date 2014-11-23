# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='damaged_objects',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=147, null=True, choices=[(b'Buildings', b'Buildings'), (b'Houses', b'Houses'), (b'Police stations', b'Police stations'), (b'Fire stations', b'Fire stations'), (b'Water supplies', b'Water supplies'), (b'Communications', b'Communications'), (b'Schools', b'Schools'), (b'Roads', b'Roads'), (b'Health facilities/hospitals', b'Health facilities/hospitals'), (b'Power supplies', b'Power supplies'), (b'Markets', b'Markets'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='impact_data_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=122, null=True, choices=[(b'Flooded area', b'Flooded area'), (b'Landslides', b'Landslides'), (b'Rainfall', b'Rainfall'), (b'Wind speeds', b'Wind speeds'), (b'Storm path', b'Storm path'), (b'Storm surge', b'Storm surge'), (b'Earthquake damage extent', b'Earthquake damage extent'), (b'Extent of conflict area', b'Extent of conflict area'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='affected_population_data_source',
            field=models.ManyToManyField(related_name='affected_population_source_for', null=True, to='maps.DataSource', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='disclaimer',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=114, null=True, choices=[(b'None', b'None'), (b'General disclaimer', b'General disclaimer'), (b'Narrative on possible errors/limitations', b'Narrative on possible errors/limitations'), (b'Uses statistical confidence measures for the data', b'Uses statistical confidence measures for the data')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='statistical_data',
            field=models.ManyToManyField(to='maps.StatisticalOrIndicatorData', null=True, blank=True),
            preserve_default=True,
        ),
    ]

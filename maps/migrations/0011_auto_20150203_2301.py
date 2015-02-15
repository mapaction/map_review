# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0010_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='basemap_image_indicator_data_source',
            field=models.ManyToManyField(related_name='basemap_image_indicator_data_source_for', null=True, to='maps.DataSource', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='explicit_target_audience_text_explanation',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='has_basemap_image_indicator_data',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='has_explicit_indication_of_target_audience',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='has_potential_target_audience',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='hunanitarian_needs_affected_population',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='potential_target_audience_text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='has_affected_pop_coping_mechanisms_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show information on coping mechanisms of the affected population/community action?', verbose_name=b'has affected population coping mechanisms data'),
            preserve_default=True,
        ),
    ]

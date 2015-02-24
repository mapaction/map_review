# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0015_auto_20150222_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='affected_pop_coping_mechanisms_data_source',
            field=models.ManyToManyField(related_name='affected_population_coping_mechanisms_source_for', null=True, to='maps.DataSource', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='is_part_of_series',
            field=models.BooleanField(default=False, help_text=b"If unsure, tick the box and select 'Unknown' below", verbose_name=b'Is or was this map part of a series?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='population_movements_data_source',
            field=models.ManyToManyField(related_name='population_movements_source_for', null=True, to='maps.DataSource', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='severity_data_source',
            field=models.ManyToManyField(related_name='severity_data_source_for', null=True, to='maps.DataSource', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='trends_evolution_data_source',
            field=models.ManyToManyField(related_name='trends_evolution_data_source_for', null=True, to='maps.DataSource', blank=True),
            preserve_default=True,
        ),
    ]

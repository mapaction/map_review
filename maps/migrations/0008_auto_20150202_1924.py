# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20150201_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='has_population_movements_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show population movement information?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='population_movements_data_date_earliest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='population_movements_data_date_latest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='population_movements_data_source',
            field=models.ManyToManyField(related_name='population_movements_source_for', to='maps.DataSource'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='source_type',
            field=models.CharField(max_length=20, choices=[(b'SATELLITE', b'Satellite data'), (b'ADMIN', b'Admin boundaries'), (b'ROADS', b'Roads'), (b'HYDRO', b'Hydrography'), (b'ELEVATION', b'Elevation'), (b'SETTLEMENTS', b'Settlements'), (b'HEALTH', b'Health facilities'), (b'SCHOOLS', b'Schools'), (b'SHELTER', b'Shelter'), (b'POPULATION', b'Population'), (b'IMPACT', b'Impact indicators/statistics'), (b'NEEDS', b'Needs'), (b'RESOURCING', b'Resourcing'), (b'GENERAL', b'General')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='has_vulnerable_population_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show information on specific vulnerabilities of the population?'),
            preserve_default=True,
        ),
    ]

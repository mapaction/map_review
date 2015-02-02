# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_auto_20150202_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='has_composite_analysis_of_severity_data',
            field=models.BooleanField(default=False, help_text=b'If so, does the map show information on severity across multiple indicators?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='has_severity_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show information of severity of impact?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='has_trends_evolution_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show analysis of trends/potential evolution of trends/potential evolution of the emergency?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='severity_data_date_earliest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='severity_data_date_latest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='severity_data_source',
            field=models.ManyToManyField(related_name='severity_data_source_for', to='maps.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='trends_evolution_data_date_earliest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='trends_evolution_data_date_latest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='trends_evolution_data_source',
            field=models.ManyToManyField(related_name='trends_evolution_data_source_for', to='maps.DataSource'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='has_vulnerable_population_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show information on specific vulnerabilities the population?'),
            preserve_default=True,
        ),
    ]

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
            name='affected_pop_coping_mechanisms_data_date_earliest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='affected_pop_coping_mechanisms_data_date_latest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='affected_pop_coping_mechanisms_data_source',
            field=models.ManyToManyField(related_name='affected_population_coping_mechanisms_source_for', to='maps.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='has_affected_pop_coping_mechanisms_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show information on coping mechanisms of theaffected population/community action?', verbose_name=b'has affected population coping mechanisms data'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='has_vulnerable_population_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show information on specific vulnerabilities the population?'),
            preserve_default=True,
        ),
    ]

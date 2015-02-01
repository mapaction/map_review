# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20141123_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='has_vulnerable_population_data',
            field=models.BooleanField(default=False, help_text=b'Does the map show information on specific vulnerabilities of the population.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='vulnerable_population_data_date_earliest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='vulnerable_population_data_date_latest',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='vulnerable_population_data_source',
            field=models.ManyToManyField(related_name='vulnerability_data_source_for', null=True, to='maps.DataSource', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='authors_or_producers',
            field=models.ManyToManyField(help_text=b"Name of the organisation(s) that authored the map - this should include all organisations acknowledged in the map marginalia by logos/name, or as part of the map title as having authored/produced the map. Organisations attributed with funding the map production should be entered in the 'Donor' field.", related_name='author_or_producer_of', to='maps.Actor'),
            preserve_default=True,
        ),
    ]

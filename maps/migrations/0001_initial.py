# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import django.core.validators
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_cluster', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_type', models.CharField(max_length=20, choices=[(b'SATELLITE', b'Satellite data'), (b'ADMIN', b'Admin boundaries'), (b'ROADS', b'Roads'), (b'HYDRO', b'Hydrography'), (b'ELEVATION', b'Elevation'), (b'SETTLEMENTS', b'Settlements'), (b'HEALTH', b'Health facilities'), (b'SHCOOLS', b'Schools'), (b'SHELTER', b'Shelter'), (b'POPULATION', b'Population'), (b'IMPACT', b'Impact indicators/statistics'), (b'NEEDS', b'Needs'), (b'RESOURCING', b'Resourcing'), (b'GENERAL', b'General')])),
                ('name', models.CharField(max_length=255)),
                ('meta', django_hstore.fields.DictionaryField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_type', models.CharField(max_length=2, choices=[(b'CW', b'Cold Wave'), (b'CE', b'Complex Emergency'), (b'DR', b'Drought'), (b'EQ', b'Earthquake'), (b'EP', b'Epidemic'), (b'EC', b'Extratropical Cyclone'), (b'ET', b'Extreme temperature (use CW/HW instead)'), (b'FA', b'Famine (use other "Hazard" code instead)'), (b'FR', b'Fire'), (b'FF', b'Flash Flood'), (b'FL', b'Flood'), (b'HT', b'Heat Wave'), (b'IN', b'Insect Infestation'), (b'LS', b'Land Slide'), (b'MS', b'Mud Slide'), (b'OT', b'Other'), (b'ST', b'SEVERE LOCAL STORM'), (b'SL', b'SLIDE (use LS/ AV/MS instead)'), (b'AV', b'Snow Avalanche'), (b'SS', b'Storm Surge'), (b'AC', b'Tech. Disaster'), (b'TO', b'Tornadoes'), (b'TC', b'Tropical Cyclone'), (b'TS', b'Tsunami'), (b'VW', b'Violent Wind'), (b'VO', b'Volcano'), (b'WV', b'Wave/Surge(use TS/SS instead)'), (b'WF', b'Wild fire')])),
                ('start_date', models.DateField()),
                ('glide_number', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{2}-[0-9]{4}-[0-9]{6}-[A-Z]{3}$', message=b"That doesn't look like a valid GLIDE number.")])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewer_name', models.CharField(max_length=300)),
                ('file_name', models.CharField(help_text=b"In case we can't attach the actual file", max_length=300, null=True, blank=True)),
                ('url', models.URLField(help_text=b'Map URL if available', null=True, blank=True)),
                ('pdf', models.FileField(help_text=b'Map file if available', null=True, upload_to=b'', blank=True)),
                ('title', models.CharField(help_text=b'Title of the map as it appears on the map', max_length=300)),
                ('language', models.CharField(help_text=b'Language used for the main information on the map (title, legend,..)', max_length=20)),
                ('production_date', models.DateField(help_text=b'Date that the map was produced, as shown on the map', null=True, blank=True)),
                ('situational_data_date', models.DateField(help_text=b'Overall date of situational data shown on map, if known.', null=True, blank=True)),
                ('day_offset', models.PositiveIntegerField(help_text=b'Number of days between disaster onset and map production.')),
                ('extent', models.CharField(help_text=b'Geographical extent of the map.', max_length=100, choices=[(b'Country', b'Country'), (b'Affected regions', b'Affected regions'), (b'Region 4B', b'Region 4B'), (b'Region 5', b'Region 5'), (b'Region 6', b'Region 6'), (b'Region 7', b'Region 7'), (b'Region 8', b'Region 8')])),
                ('is_part_of_series', models.BooleanField(default=False, help_text=b'Is/was the map part of a regularly udpated series?')),
                ('update_frequency', models.CharField(help_text=b'If the map was part of a series, approximately how frequently was it updated?', max_length=10, choices=[(b'DAILY', b'Daily')])),
                ('infographics', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=43, null=True, help_text=b'Infographics or other non-map items in map.', choices=[(b'Infographic', b'Infographic'), (b'Pie chart', b'Pie chart'), (b'Bar chart', b'Bar chart'), (b'Table', b'Table'), (b'Other', b'Other')])),
                ('disclaimer', models.TextField(null=True, blank=True)),
                ('copyright', models.TextField(null=True, blank=True)),
                ('has_satellite_data', models.BooleanField(default=False)),
                ('phase_type', models.CharField(help_text=b'Is it pre or post disaster imagery?', max_length=255, null=True, blank=True)),
                ('satellite_data_date', models.DateField(null=True, blank=True)),
                ('has_admin_boundaries', models.BooleanField(default=False)),
                ('admin_max_detail_level', models.CharField(max_length=50, null=True, blank=True)),
                ('has_roads', models.BooleanField(default=False)),
                ('has_hydrographic_network', models.BooleanField(default=False)),
                ('has_elevation_data', models.BooleanField(default=False)),
                ('elevation_data_type', models.CharField(max_length=50, null=True, blank=True)),
                ('has_settlements_data', models.BooleanField(default=False)),
                ('settlements_max_detail_level', models.CharField(max_length=50, null=True, blank=True)),
                ('settlements_data_type', models.CharField(max_length=50, null=True, blank=True)),
                ('has_health_data', models.BooleanField(default=False)),
                ('has_schools_data', models.BooleanField(default=False)),
                ('has_shelter_data', models.BooleanField(default=False)),
                ('shelter_data_date', models.DateField(null=True, blank=True)),
                ('has_impact_geographic_extent', models.BooleanField(default=False)),
                ('impact_data_source_type', models.CharField(blank=True, max_length=20, null=True, choices=[(b'MODEL', b'Modelled/predicted'), (b'OBSERVATION', b'Observed')])),
                ('impact_situational_date_earliest', models.DateField(null=True, blank=True)),
                ('impact_situational_date_latest', models.DateField(null=True, blank=True)),
                ('damage_situational_date_earliest', models.DateField(null=True, blank=True)),
                ('damage_situational_date_latest', models.DateField(null=True, blank=True)),
                ('has_population_data', models.BooleanField(default=False)),
                ('population_data_type', models.CharField(max_length=50, null=True, blank=True)),
                ('population_data_date_earliest', models.DateField(null=True, blank=True)),
                ('population_data_date_latest', models.DateField(null=True, blank=True)),
                ('has_affected_population_data', models.BooleanField(default=False)),
                ('affected_population_data_date_earliest', models.DateField(null=True, blank=True)),
                ('affected_population_data_date_latest', models.DateField(null=True, blank=True)),
                ('has_statistical_data', models.BooleanField(default=False)),
                ('has_subcluster_information', models.BooleanField(default=False)),
                ('has_activity_detail', models.BooleanField(default=False)),
                ('has_humanitarian_needs', models.BooleanField(default=False)),
                ('humanitarian_needs_data_date_earliest', models.DateField(null=True, blank=True)),
                ('humanitarian_needs_data_date_latest', models.DateField(null=True, blank=True)),
                ('resourcing_data_date_earliest', models.DateField(null=True, blank=True)),
                ('resourcing_data_date_latest', models.DateField(null=True, blank=True)),
                ('indirect_datasets', models.TextField(null=True, blank=True)),
                ('admin_data_source', models.ForeignKey(related_name='admin_source_for', blank=True, to='maps.DataSource', null=True)),
                ('affected_population_data_source', models.ManyToManyField(related_name='affected_population_source_for', to='maps.DataSource')),
                ('authors_or_producers', models.ManyToManyField(help_text=b"Name of the organisation(s) that authored the map - thisshould include all organisations acknowledged in the map marginalia by logos/name, or as part of the map title as having authored/produced the map. Organisations attributed with funding the map production should be entered in the 'Donor' field.", related_name='author_or_producer_of', to='maps.Actor')),
                ('donors', models.ManyToManyField(help_text=b'Organisation(s) attributed with funding the map production.', related_name='donor_to', to='maps.Actor')),
                ('elevation_data_source', models.ForeignKey(related_name='elevation_source_for', blank=True, to='maps.DataSource', null=True)),
                ('event', models.ForeignKey(to='maps.Event')),
                ('health_data_source', models.ForeignKey(related_name='health_source_for', blank=True, to='maps.DataSource', null=True)),
                ('humanitarian_needs_data_source', models.ForeignKey(related_name='humanitarian_needs_source_for', blank=True, to='maps.DataSource', null=True)),
                ('hydrographic_data_source', models.ForeignKey(related_name='hydrographic_source_for', blank=True, to='maps.DataSource', null=True)),
                ('population_data_source', models.ForeignKey(related_name='population_source_for', blank=True, to='maps.DataSource', null=True)),
                ('roads_data_source', models.ForeignKey(related_name='roads_source_for', blank=True, to='maps.DataSource', null=True)),
                ('satellite_data_source', models.ForeignKey(related_name='satellite_source_for', blank=True, to='maps.DataSource', null=True)),
                ('schools_data_source', models.ForeignKey(related_name='schools_source_for', blank=True, to='maps.DataSource', null=True)),
                ('settlements_data_source', models.ForeignKey(related_name='settlements_source_for', blank=True, to='maps.DataSource', null=True)),
                ('shelter_data_source', models.ForeignKey(related_name='shelter_source_for', blank=True, to='maps.DataSource', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StatisticalOrIndicatorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_type', models.CharField(max_length=255, null=True, blank=True)),
                ('is_pre_or_post', models.CharField(blank=True, max_length=50, null=True, choices=[(b'PRE', b'Pre-event'), (b'POST', b'Post-event')])),
                ('data_date_earliest', models.DateField(null=True, blank=True)),
                ('data_date_latest', models.DateField(null=True, blank=True)),
                ('data_source', models.ForeignKey(related_name='stats_source_for', blank=True, to='maps.DataSource', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='map',
            name='statistical_data',
            field=models.ManyToManyField(to='maps.StatisticalOrIndicatorData'),
            preserve_default=True,
        ),
    ]

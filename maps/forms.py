# -*- coding: utf-8 -*-
from django import forms
from django.db import models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from crispy_forms.bootstrap import FormActions

from .models import Map


def fields_of(indicator, *fields):
    """Sets fields to depend on indicator (adds data-depends-on attr).

    :param str indicator: Name of field upon which others depend.
    :param str *fields: field names which depend upon indicator.
    :rtype: list
    :return: list of field objects

    """
    ret = [
        Field(indicator, data_indicator=indicator)
    ]
    for f in fields:
        kwargs = {}
        model_field = Map._meta.get_field_by_name(f)[0]
        if any([
                isinstance(model_field, models.ManyToManyField),
                isinstance(model_field, models.ForeignKey),
                (isinstance(model_field, models.CharField) and
                 hasattr(model_field, 'choices'))]):
            kwargs['css_class'] = 'chosen'

        ret.append(
            Field(
                f, data_depends_on=indicator, wrapper_class=indicator,
                **kwargs
            )
        )
    return ret


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Map

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        # The default widget is a checkbox one, but we want to use chosen
        # so revert to regular select:
        for f in self.fields:
            if isinstance(self.fields[f].widget, forms.CheckboxSelectMultiple):
                self.fields[f].widget = forms.SelectMultiple(
                    choices=self.fields[f].choices
                )
        self.helper = FormHelper()

        geo_field_groups_by_indicator = []
        geo_field_groups_by_indicator.extend(fields_of(
            'has_satellite_data',
            'phase_type',
            'satellite_data_date',
            'satellite_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_admin_boundaries',
            'admin_max_detail_level',
            'admin_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_roads',
            'roads_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_hydrographic_network',
            'hydrographic_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_elevation_data',
            'elevation_data_type',
            'elevation_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_settlements_data',
            'settlements_max_detail_level',
            'settlements_data_type',
            'settlements_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_health_data',
            'health_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_schools_data',
            'schools_data_source',
        ))
        geo_field_groups_by_indicator.extend(fields_of(
            'has_shelter_data',
            'shelter_data_source',
            'shelter_data_date',
        ))

        pop_field_groups_by_indicator = []
        pop_field_groups_by_indicator.extend(fields_of(
            'has_population_data',
            'population_data_type',
            'population_data_source',
            'population_data_date_earliest',
            'population_data_date_latest',
        ))

        pop_field_groups_by_indicator.extend(fields_of(
            'has_affected_population_data',
            'humanitarian_profile_level_1_types',
            'disaggregated_affected_population_types',
            'affected_population_data_date_earliest',
            'affected_population_data_date_latest',
            'affected_population_data_source',
        ))

#       # TODO: Needs activities gaps
#        field_groups_by_indicator.extend(fields_of(
#            # TODO: active_clusters
#            'has_subcluster_information',
#            'has_activity_detail',
#            # TODO: assessments

#       # TODO: Additional data sources
#       # TODO: General data sources

        self.helper.layout = Layout(
            Fieldset(
                'Reviewer details',
                Field('reviewer_name', title='Your name'),
            ),
            Fieldset(
                'Map file/location details',
                'file_name',
                'url',
                'pdf',
            ),
            Fieldset(
                'General map information',
                'title',
                'language',
                Field('event', css_class='chosen'),
                'production_date',
                'situational_data_date',
                'day_offset',
                Field('extent', css_class='chosen'),
                Field('authors_or_producers', css_class='chosen'),
                Field('donors', css_class='chosen'),
                'is_part_of_series',
                Field('update_frequency', css_class='chosen'),
                Field('infographics', css_class='chosen'),
                Field('disclaimer', css_class='chosen'),
                'copyright',
            ),
            Fieldset(
                'Geographic data',
                *geo_field_groups_by_indicator
            ),
            Fieldset(
                'Impact data',
                *fields_of(
                    'has_impact_geographic_extent',
                    'impact_data_types',
                    'impact_data_source_type',
                    'impact_situational_date_earliest',
                    'impact_situational_date_latest',
                    'damaged_objects',
                    'damage_situational_date_earliest',
                    'damage_situational_date_latest',
                )
            ),
            Fieldset(
                'Population data',
                *pop_field_groups_by_indicator
            ),
            Fieldset(
                'Indicators/statistics',
                *fields_of(
                    'has_statistical_data',
                    'statistical_data',
                )
            ),
            FormActions(
                Submit('save', 'Save changes'),
            )
        )

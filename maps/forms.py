# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

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

        # Make date pickers pretty
        if f.endswith('date'):
            kwargs['template'] = 'maps/date_component.html'

        # Make date ranges look a bit more rangey
        if (f.endswith('date_earliest') and
                f.replace('earliest', 'latest') in fields):
            kwargs['template'] = 'maps/date_range.html'
            kwargs['title'] = model_field.verbose_name.replace(
                ' earliest', '').title()
            kwargs['data_latest'] = f.replace('earliest', 'latest')
            kwargs['css_class'] = 'date-earliest'

        if (f.endswith('date_latest') and
                f.replace('latest', 'earliest') in fields):
            kwargs['type'] = 'hidden'
            kwargs['data_earliest'] = f.replace('latest', 'earliest')

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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.group = kwargs.pop('group', None)
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        # The default widget is a checkbox one, but we want to use chosen
        # so revert to regular select:
        for f in self.fields:
            if isinstance(self.fields[f].widget, forms.CheckboxSelectMultiple):
                self.fields[f].widget = forms.SelectMultiple(
                    choices=self.fields[f].choices
                )
        self.helper = FormHelper()
        self.helper.help_text_inline = True

        decision_making_field_groups_by_indicator = []
        decision_making_field_groups_by_indicator.extend(fields_of(
            'has_explicit_indication_of_target_audience',
            'explicit_target_audience_text_explanation',
        ))
        decision_making_field_groups_by_indicator.extend(fields_of(
            'has_potential_target_audience',
            'potential_target_audience_text',
        ))

        geo_field_groups_by_indicator = []
        geo_field_groups_by_indicator.extend(fields_of(
            'has_basemap_image_indicator_data',
            'basemap_image_indicator_data_source',
        ))
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

        pop_field_groups_by_indicator.extend(fields_of(
            'has_vulnerable_population_data',
            'vulnerable_population_data_date_earliest',
            'vulnerable_population_data_date_latest',
            'vulnerable_population_data_source',
        ))

        pop_field_groups_by_indicator.extend(fields_of(
            'has_affected_pop_coping_mechanisms_data',
            'affected_pop_coping_mechanisms_data_date_earliest',
            'affected_pop_coping_mechanisms_data_date_latest',
            'affected_pop_coping_mechanisms_data_source',
        ))

        pop_field_groups_by_indicator.extend(fields_of(
            'has_population_movements_data',
            'population_movements_data_date_earliest',
            'population_movements_data_date_latest',
            'population_movements_data_source',
        ))

        severity_field_groups_by_indicator = []
        severity_field_groups_by_indicator.extend(fields_of(
            'has_severity_data',
            'has_composite_analysis_of_severity_data',
            'severity_data_date_earliest',
            'severity_data_date_latest',
            'severity_data_source',
        ))

        severity_field_groups_by_indicator.extend(fields_of(
            'has_trends_evolution_data',
            'trends_evolution_data_date_earliest',
            'trends_evolution_data_date_latest',
            'trends_evolution_data_source',
        ))

#       # TODO: Needs activities gaps
#        field_groups_by_indicator.extend(fields_of(
#            # TODO: active_clusters
#            'has_subcluster_information',
#            'has_activity_detail',
#            # TODO: assessments

#       # TODO: Additional data sources
#       # TODO: General data sources

        map_meta = []
        if self.group is None or self.group.allow_pdf_uploads:
            map_meta.append('file_name')
            map_meta.append('pdf')
        if self.group is None or self.group.need_url_links:
            map_meta.append(
                Field(
                    'url',
                    help_text="URL on ReliefWeb is map posted there."
                )
            )

        self.helper.layout = Layout(
            Fieldset(
                'Reviewer details',
                Field('reviewer_name', title='Your name'),
                Field('reviewer_email', title='Your email address'),
            ),
            Fieldset(
                'Map file/location details',
                *map_meta
            ),
            Fieldset(
                'General map information',
                'title',
                'language',
                Field('event', css_class='chosen'),
                Field('production_date', template="maps/date_component.html"),
                Field(
                    'situational_data_date',
                    template="maps/date_component.html"),
                'day_offset',
                Field('extent', css_class='chosen'),
                Field('authors_or_producers', css_class='chosen'),
                Field('donors', css_class='chosen'),
                Field('infographics', css_class='chosen'),
                Field('disclaimer', css_class='chosen'),
                'copyright',
            ),
            Fieldset(
                'Series',
                *fields_of(
                    'is_part_of_series',
                    'update_frequency',
                )
            ),
            Fieldset(
                'Decision making / Audience target data',
                *decision_making_field_groups_by_indicator
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
                'Severity, Analysis and Evolution data',
                *severity_field_groups_by_indicator
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

        # If this is a grouped review, lock some fields
        lock_for_group = (
            self.group and self.initial and 'event' in self.initial)
        if lock_for_group:
            self.fields['event'].widget.attrs['readonly'] = True
            self.fields['event'].widget.attrs['disabled'] = True
            self.fields['extent'].choices = self.group.get_extent_options()

        if self.group is not None and self.group.map_url_help_text:
            self.fields['url'].help_text = self.group.map_url_help_text

        if self.group is not None and self.group.admin_levels_help_text:
            self.fields['admin_max_detail_level'].help_text = (
                self.group.admin_levels_help_text
            )

        for field in self.fields:
            f = self.fields[field]
            if (isinstance(f, forms.MultipleChoiceField) or
                    isinstance(f, forms.ModelMultipleChoiceField)):
                f.widget.attrs['data-placeholder'] = _('Select Option(s)')
                # Workaround for obnoxious Django field see bug
                # https://code.djangoproject.com/ticket/9321
                if f.help_text.find('Hold down ') > -1:
                    f.help_text = f.help_text[:f.help_text.find('Hold down ')]
            if field.endswith('date_earliest'):
                f.label = f.label.replace(' earliest', '')
                f.help_text = _(
                    "Enter earliest and latest date, or just one or the other."
                )

from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django_hstore import hstore

from multiselectfield import MultiSelectField


def make_choices(*choices):
    """Just dupes choices name/value"""
    return [(c, c) for c in choices]


DATA_TYPES = make_choices(
    'Points',
    'Polygons',
    'Bar/pie charts',
    'Raster density',
    'Infographics',
    'Other',
)


class Actor(models.Model):
    """An actor in the scene."""
    is_cluster = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        if self.is_cluster:
            return u"Cluster: " + self.name
        return self.name


class Event(models.Model):
    """Represents an event (disaster)."""
    EVENT_OPTIONS = (
        ("CW", "Cold Wave"),
        ("CE", "Complex Emergency"),
        ("DR", "Drought"),
        ("EQ", "Earthquake"),
        ("EP", "Epidemic"),
        ("EC", "Extratropical Cyclone"),
        ("ET", "Extreme temperature (use CW/HW instead)"),
        ("FA", "Famine (use other \"Hazard\" code instead)"),
        ("FR", "Fire"),
        ("FF", "Flash Flood"),
        ("FL", "Flood"),
        ("HT", "Heat Wave"),
        ("IN", "Insect Infestation"),
        ("LS", "Land Slide"),
        ("MS", "Mud Slide"),
        ("OT", "Other"),
        ("ST", "SEVERE LOCAL STORM"),
        ("SL", "SLIDE (use LS/ AV/MS instead)"),
        ("AV", "Snow Avalanche"),
        ("SS", "Storm Surge"),
        ("AC", "Tech. Disaster"),
        ("TO", "Tornadoes"),
        ("TC", "Tropical Cyclone"),
        ("TS", "Tsunami"),
        ("VW", "Violent Wind"),
        ("VO", "Volcano"),
        ("WV", "Wave/Surge(use TS/SS instead)"),
        ("WF", "Wild fire"),
    )
    event_type = models.CharField(max_length=2, choices=EVENT_OPTIONS)
    start_date = models.DateField()
    # TODO: Improve regex
    glide_number = models.CharField(
        max_length=18,
        validators=[RegexValidator(
            regex=r'^[A-Z]{2}-[0-9]{4}-[0-9]{6}-[A-Z]{3}$',  # approx.
            message="That doesn't look like a valid GLIDE number."
        )]
    )

    def __unicode__(self):
        return("{0}, {1}".format(
            self.get_event_type_display(), self.glide_number
        ))


class DataSource(models.Model):
    """Any of various data sources. Use meta to store extra info."""
    source_type = models.CharField(
        choices=(
            ('SATELLITE', 'Satellite data'),
            ('ADMIN', 'Admin boundaries'),
            ('ROADS', 'Roads'),
            ('HYDRO', 'Hydrography'),
            ('ELEVATION', 'Elevation'),
            ('SETTLEMENTS', 'Settlements'),
            ('HEALTH', 'Health facilities'),
            ('SCHOOLS', 'Schools'),
            ('SHELTER', 'Shelter'),
            ('POPULATION', 'Population'),
            ('IMPACT', 'Impact indicators/statistics'),
            ('NEEDS', 'Needs'),
            ('RESOURCING', 'Resourcing'),
            ('GENERAL', 'General')
        ), max_length=20,
    )
    name = models.CharField(max_length=255)
    meta = hstore.DictionaryField()

    def __unicode__(self):
        return "{0} - {1}".format(self.source_type, self.name)


class StatisticalOrIndicatorData(models.Model):
    data_type = models.CharField(
        max_length=255,
        null=True, blank=True,
    )
    is_pre_or_post = models.CharField(
        choices=(
            ('PRE', 'Pre-event'),
            ('POST', 'Post-event'),
        ),
        max_length=50,
        null=True, blank=True,
    )
    data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    data_date_latest = models.DateField(
        null=True, blank=True,
    )
    data_source = models.ForeignKey(
        DataSource,
        related_name="stats_source_for",
        null=True, blank=True,
    )


class ReviewGroup(models.Model):
    """For creating specific event reviews (eg. Haiyan) w/custom settings."""
    contact = models.ForeignKey(
        User, help_text="Admin contact who should deal with data requests.")
    top_copy = models.TextField(
        help_text="Add HTML here about this set of reviews.")
    event = models.ForeignKey(
        Event, help_text="Which event are these reviews for?")
    name = models.CharField(
        max_length=100,
        help_text="Friendly name for this grouping "
        "(eg. Typhoon Haiyan - Philippines)"
    )
    slug = models.SlugField()

    # TODO: This really ought to be a M2M to some sensible regions table.
    extent_options = models.TextField(
        help_text="Specify what should appear in the Extent dropdown "
        "(one per line)."
    )

    allow_pdf_uploads = models.BooleanField(default=False)
    need_url_links = models.BooleanField(
        default=True,
        help_text="Should the Reviewer link to the map they reviewed? "
        "If they are not uploading a map, they likely should."
    )
    map_url_help_text = models.CharField(
        help_text="Where should the reviewer link to? (E.g. ReliefWeb)",
        max_length=200,
        blank=True, null=True
    )

    def __unicode__(self):
        return u"{} -- {}".format(self.name, self.event.glide_number)

    def get_extent_options(self):
        return [
            (x, x) for x in self.extent_options.split('\n')
        ]


class ExtentMultiSelectField(MultiSelectField):
    def validate(self, value, model_instance):
        pass


class Map(models.Model):
    """Storage of a Map object."""
    review_created_on = models.DateTimeField(auto_now_add=True)
    reviewer_name = models.CharField(
        'Reviewer full name',
        max_length=300,
    )
    reviewer_email = models.EmailField(
        'Reviewer email address',
        help_text="For our records. This will not be shared outside of the "
        "partner organisations."
    )
    file_name = models.CharField(
        max_length=300, blank=True, null=True,
        help_text="In case we can't attach the actual file"
    )
    url = models.URLField(
        'Map URL',
        blank=True, null=True,
        help_text="Map URL if available"
    )
    pdf = models.FileField(
        blank=True, null=True,
        help_text="Map file if available"
    )

    title = models.CharField(
        max_length=300,
        help_text="Title of the map as it appears on the map"
    )
    language = models.CharField(
        max_length=20,
        help_text="Language used for the main information on the map "
        "(title, legend,..)"
    )
    event = models.ForeignKey(Event)

    production_date = models.DateField(
        help_text="Date that the map was produced, as shown on the map",
        null=True, blank=True
    )
    situational_data_date = models.DateField(
        help_text="Overall date of situational data shown on map, if known.",
        null=True, blank=True
    )
    day_offset = models.PositiveIntegerField(
        help_text="Number of days between disaster onset and map production."
    )
    # TODO: This really ought to be a M2M to some sensible regions table.
    extent = ExtentMultiSelectField(
        help_text="Geographical extent of the map.",
        choices=make_choices('Country', 'Affected areas')
    )

    authors_or_producers = models.ManyToManyField(
        Actor,
        related_name='author_or_producer_of',
        help_text="Name of the organisation(s) that authored the map - this "
        "should include all organisations acknowledged in the map marginalia "
        "by logos/name, or as part of the map title as having "
        "authored/produced the map. Organisations attributed with funding the "
        "map production should be entered in the 'Donor' field.",
    )
    donors = models.ManyToManyField(
        Actor,
        related_name='donor_to',
        help_text="Organisation(s) attributed with funding the map "
        "production."
    )
    is_part_of_series = models.BooleanField(
        "Is or was this map part of a series?",
        default=False,
        help_text="If you are not sure, tick the box and select 'Unknown' below"
    )
    update_frequency = models.CharField(
        max_length=10,
        choices=make_choices(
            'Unknown',
            'Daily',
            'Weekly',
            'Monthly',
            'Other',
        ),
        help_text="If the map was part of a series, approximately how "
        "frequently was it updated?",
        null=True, blank=True
    )
    # TODO: infographics indicated to be choice list, with multiples possible.
    # Not sure what these choices are (per map?)
    infographics = MultiSelectField(
        choices=make_choices(
            'Infographic',
            'Pie chart',
            'Bar chart',
            'Table',
            'Other',
        ),
        help_text="List of infographics or other non-map items appearing on the"
        " map",
        null=True, blank=True
    )
    disclaimer = MultiSelectField(
        choices=make_choices(
            'None',
            'General disclaimer',
            'Narrative on possible errors/limitations',
            'Uses statistical confidence measures for the data',
        ),
        null=True, blank=True,
        help_text="Type of disclaimer appearing on the map"
    )
    copyright = models.TextField(
        null=True, blank=True
    )

    # Decision Making/Audience targets group
    # Decision making/audience targets
    has_explicit_indication_of_target_audience = models.BooleanField(
        default=False
    )
    explicit_target_audience_text_explanation = models.TextField(
        blank=True, null=True,
    )
    has_potential_target_audience = models.BooleanField(default=False)
    potential_target_audience_text = models.TextField(blank=True, null=True)

    # Geographic Data Block
    # Basemap image group
    has_basemap_image_indicator_data = models.BooleanField(default=False)
    basemap_image_indicator_data_source = models.ManyToManyField(
        DataSource,
        related_name="basemap_image_indicator_data_source_for",
        null=True, blank=True,
    )

    # Satellite data group
    has_satellite_data = models.BooleanField(default=False)
    phase_type = models.CharField(
        help_text="Is it pre or post disaster imagery?",
        max_length=255,
        choices=make_choices(
            'Pre-disaster',
            'Post-disaster',
        ),
        null=True, blank=True,
    )
    satellite_data_date = models.DateField(null=True, blank=True)
    satellite_data_source = models.ForeignKey(
        DataSource,
        related_name="satellite_source_for",
        null=True, blank=True
    )

    # Admin boundaries group
    has_admin_boundaries = models.BooleanField(default=False)
    admin_max_detail_level = models.CharField(
        choices=make_choices(
            'Regions (Level 1)',
            'Provinces (Level 2)',
            'Municipalities (Level 3)',
            'Barangays (Level 4)',
        ), max_length=50,
        null=True, blank=True,
    )
    admin_data_source = models.ForeignKey(
        DataSource,
        related_name="admin_source_for",
        null=True, blank=True,
    )

    # Roads group
    has_roads = models.BooleanField(default=False)
    roads_data_source = models.ForeignKey(
        DataSource,
        related_name="roads_source_for",
        null=True, blank=True,
    )

    # Hydrography group
    has_hydrographic_network = models.BooleanField(default=False)
    hydrographic_data_source = models.ForeignKey(
        DataSource,
        related_name="hydrographic_source_for",
        null=True, blank=True,
    )

    # Elevation group
    has_elevation_data = models.BooleanField(default=False)
    elevation_data_type = models.CharField(
        choices=make_choices(
            'Point heights',
            'Contour lines',
            'DEM (continuous surface)',
        ), max_length=50,
        null=True, blank=True,
    )
    elevation_data_source = models.ForeignKey(
        DataSource,
        related_name="elevation_source_for",
        null=True, blank=True,
    )

    # Settlements group
    has_settlements_data = models.BooleanField(default=False)
    settlements_max_detail_level = models.CharField(
        choices=make_choices(
            'Main cities',
            'Towns',
            'Villages',
            'Individual buildings',
        ), max_length=50,
        null=True, blank=True,
    )
    settlements_data_type = models.CharField(
        choices=DATA_TYPES, max_length=50,
        null=True, blank=True,
    )
    settlements_data_source = models.ForeignKey(
        DataSource,
        related_name="settlements_source_for",
        null=True, blank=True,
    )

    # Health group
    has_health_data = models.BooleanField(default=False)
    health_data_source = models.ForeignKey(
        DataSource,
        related_name="health_source_for",
        null=True, blank=True,
    )

    # Schools group
    has_schools_data = models.BooleanField(default=False)
    schools_data_source = models.ForeignKey(
        DataSource,
        related_name="schools_source_for",
        null=True, blank=True,
    )

    # Shelter group
    has_shelter_data = models.BooleanField(default=False)
    shelter_data_source = models.ForeignKey(
        DataSource,
        related_name="shelter_source_for",
        null=True, blank=True,
    )
    shelter_data_date = models.DateField(
        null=True, blank=True,
    )

    # Physical impact block
    # Physical impact group
    has_impact_geographic_extent = models.BooleanField(default=False)
    impact_data_types = MultiSelectField(
        choices=make_choices(
            'Flooded area',
            'Landslides',
            'Rainfall',
            'Wind speeds',
            'Storm path',
            'Storm surge',
            'Earthquake damage extent',
            'Extent of conflict area',
            'Other',
        ),
        null=True, blank=True,
    )
    impact_data_source_type = models.CharField(
        choices=(
            ('MODEL', 'Modelled/predicted'),
            ('OBSERVATION', 'Observed'),
        ), max_length=20,
        null=True, blank=True,
    )
    impact_situational_date_earliest = models.DateField(
        null=True, blank=True,
    )
    impact_situational_date_latest = models.DateField(
        null=True, blank=True,
    )

    # Damage group
    damaged_objects = MultiSelectField(
        choices=make_choices(
            'Buildings',
            'Houses',
            'Police stations',
            'Fire stations',
            'Water supplies',
            'Communications',
            'Schools',
            'Roads',
            'Health facilities/hospitals',
            'Power supplies',
            'Markets',
            'Other',
        ),
        null=True, blank=True,
    )
    damage_situational_date_earliest = models.DateField(
        null=True, blank=True,
    )
    damage_situational_date_latest = models.DateField(
        null=True, blank=True,
    )

    # Population data, affected groups and humanitarian profile block
    # Population group
    has_population_data = models.BooleanField(default=False)
    population_data_type = models.CharField(
        choices=DATA_TYPES,
        max_length=50,
        null=True, blank=True,
    )
    population_data_source = models.ForeignKey(
        DataSource,
        related_name="population_source_for",
        null=True, blank=True,
    )
    population_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    population_data_date_latest = models.DateField(
        null=True, blank=True,
    )

    # Affected population group
    has_affected_population_data = models.BooleanField(default=False)
    humanitarian_profile_level_1_types = MultiSelectField(
        choices=make_choices(
            'Numbers of dead',
            'Numbers of missing/injured',
            'Numbers of displaced',
            'Number affected but not displaced',
            'Other',
        ),
        null=True, blank=True,
    )
    disaggregated_affected_population_types = MultiSelectField(
        choices=make_choices(
            'Age',
            'Gender',
            'Other',
        ),
        null=True, blank=True,
    )
    affected_population_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    affected_population_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    affected_population_data_source = models.ManyToManyField(
        DataSource,
        related_name="affected_population_source_for",
        null=True, blank=True,
    )

    # Vulnerability group
    has_vulnerable_population_data = models.BooleanField(
        default=False,
        help_text="Does the map show information on specific vulnerabilities "
        "the population?"
    )
    vulnerable_population_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    vulnerable_population_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    vulnerable_population_data_source = models.ManyToManyField(
        DataSource,
        related_name="vulnerability_data_source_for",
        null=True, blank=True,
    )

    # Population movements group
    has_population_movements_data = models.BooleanField(
        default=False,
        help_text="Does the map show population movement information?"
    )
    population_movements_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    population_movements_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    population_movements_data_source = models.ManyToManyField(
        DataSource,
        related_name="population_movements_source_for",
    )

    # Affected population coping mechanisms group
    has_affected_pop_coping_mechanisms_data = models.BooleanField(
        default=False,
        help_text="Does the map show information on coping mechanisms of the "
        "affected population/community action?",
        verbose_name="has affected population coping mechanisms data"
    )
    affected_pop_coping_mechanisms_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    affected_pop_coping_mechanisms_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    affected_pop_coping_mechanisms_data_source = models.ManyToManyField(
        DataSource,
        related_name="affected_population_coping_mechanisms_source_for"
    )

    # Severity, analyses and evolution block
    # Severity, and composite analysis group
    has_severity_data = models.BooleanField(
        default=False,
        help_text="Does the map show information of severity of impact?"
    )
    has_composite_analysis_of_severity_data = models.BooleanField(
        default=False,
        help_text="If so, does the map show information on severity across "
        "multiple indicators?"
    )
    severity_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    severity_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    severity_data_source = models.ManyToManyField(
        DataSource,
        related_name="severity_data_source_for",
    )

    # Trends/Evolution group
    has_trends_evolution_data = models.BooleanField(
        default=False,
        help_text="Does the map show analysis of trends/potential evolution "
        "of trends/potential evolution of the emergency?"
    )
    trends_evolution_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    trends_evolution_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    trends_evolution_data_source = models.ManyToManyField(
        DataSource,
        related_name="trends_evolution_data_source_for",
    )

    # Inidicators / Statistics block
    # Statistical data group
    has_statistical_data = models.BooleanField(default=False)
    statistical_data = models.ManyToManyField(
        StatisticalOrIndicatorData,
        null=True, blank=True,
    )

    # Needs, activites & gaps block
    # TODO:
#    active_clusters = models.ManyToManyField(
#        Cluster
#    )
    has_subcluster_information = models.BooleanField(default=False)
    has_activity_detail = models.BooleanField(default=False)
    # TODO:
#    assessments = models.ManyToManyField(
#        Assessment
#    )
    # Needs group
    has_humanitarian_needs = models.BooleanField(default=False)
    hunanitarian_needs_affected_population = models.TextField(
        blank=True, null=True,
    )
    humanitarian_needs_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    humanitarian_needs_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    humanitarian_needs_data_source = models.ForeignKey(
        DataSource,
        related_name="humanitarian_needs_source_for",
        null=True, blank=True,
    )
    # TODO
#    gaps = models.ManyToManyField(
#        Gap
#        max_length=50,
#    )
#    resourcing_or_funding = models.ManyToManyField(
#        ResourceOrFund,
#        max_length=50,
#    )
    resourcing_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    resourcing_data_date_latest = models.DateField(
        null=True, blank=True,
    )

    # Other
#    # TODO
#    additional_datasets = models.ManyToManyField(
#        AdditionalDataset
#    )
    indirect_datasets = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('maps_detail', kwargs={'pk': self.pk})

    def get_reviewer_name_sensitive(self):
        """Don't show whole name to the world."""
        return self.reviewer_name.split(' ')[0][:10]

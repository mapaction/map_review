from django.db import models
from django.core.validators import RegexValidator
from django_hstore import hstore


# TODO: Not sure what this should contain?
UPDATE_FREQUENCY_CHOICES = (
    ('DAILY', 'Daily'),
)


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


class DataSource(models.Model):
    """Satellite name and sensor type."""
    source_type = models.CharField(
        choices=(
            ('SATELLITE', 'Satellite data'),
            ('ADMIN', 'Admin boundaries'),
            ('ROADS', 'Roads'),
            ('HYDRO', 'Hydrography'),
            ('ELEVATION', 'Elevation'),
            ('SETTLEMENTS', 'Settlements'),
            ('HEALTH', 'Health facilities'),
            ('SHCOOLS', 'Schools'),
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
        return "{0} - {1}".format(self.name, self.sensor_type)


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


class Map(models.Model):
    """Storage of a Map object."""
    reviewer_name = models.CharField(max_length=300)
    file_name = models.CharField(
        max_length=300, blank=True, null=True,
        help_text="In case we can't attach the actual file"
    )
    url = models.URLField(
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
    # TODO: Extent indicated to be choice list, with multiples possible.
    # Not sure what these choices are (per map?)
    extent = models.CharField(
        help_text="Geographical extent of the map.",
        choices=(),
        max_length=100,
    )

    authors_or_producers = models.TextField(
        help_text="Name of the organisation(s) that authored the map - this"
        "should include all organisations acknowledged in the map marginalia "
        "by logos/name, or as part of the map title as having "
        "authored/produced the map. Organisations attributed with funding the "
        "map production should be entered in the 'Donor' field."
    )
    donor = models.TextField(
        help_text="Organisation(s) attributed with funding the map "
        "production."
    )
    is_part_of_series = models.BooleanField(
        default=False,
        help_text="Is/was the map part of a regularly udpated series?"
    )
    update_frequency = models.CharField(
        max_length=10,
        choices=UPDATE_FREQUENCY_CHOICES,
        help_text="If the map was part of a series, approximately how "
        "frequently was it updated?"
    )
    # TODO: infographics indicated to be choice list, with multiples possible.
    # Not sure what these choices are (per map?)
    infographics = models.TextField(
        help_text="Infographics or other non-map items in map.",
        null=True, blank=True
    )
    disclaimer = models.TextField(
        null=True, blank=True
    )
    copyright = models.TextField(
        null=True, blank=True
    )

    # Satellite data group
    has_satellite_data = models.BooleanField(default=False)
    phase_type = models.CharField(
        help_text="Is it pre or post disaster imagery?",
        max_length=255, choices=(),
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
        choices=(), max_length=50,
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
        choices=(), max_length=50,
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
        choices=(), max_length=50,
        null=True, blank=True,
    )
    settlements_data_type = models.CharField(
        choices=(), max_length=50,
        null=True, blank=True,
    )
    settlements_data_source = models.ForeignKey(
        DataSource,
        related_name="settlements_source_for",
        null=True, blank=True,
    )

    # Health data
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

    # Physical impact
    has_impact_geographic_extent = models.BooleanField(default=False)
    #    TODO
#    impact_data_types = models.ManyToManyField(
#        ImpactDataType
#    )
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
    #    TODO:
#    damaged_objects = models.ManyToManyField(
#        ObjectType
#    )
    damage_situational_date_earliest = models.DateField(
        null=True, blank=True,
    )
    damage_situational_date_latest = models.DateField(
        null=True, blank=True,
    )

    # Population group
    has_population_data = models.BooleanField(default=False)
    population_data_type = models.CharField(
        choices=(),
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

    has_affected_population_data = models.BooleanField(default=False)
    # TODO:
#    humanitarian_profile_level_1_types = models.ManyToManyField(
#        HumanitarianProfileLevelType
#    )
#    disaggregated_affected_population_types = models.ManyToManyField(
#        DisaggregatedAffectedPopulationType
#    )

    affected_population_data_date_earliest = models.DateField(
        null=True, blank=True,
    )
    affected_population_data_date_latest = models.DateField(
        null=True, blank=True,
    )
    affected_population_data_source = models.ManyToManyField(
        DataSource,
        related_name="affected_population_source_for",
    )

    # Statistical data
    has_statistical_data = models.BooleanField(default=False)
    statistical_data = models.ManyToManyField(
        StatisticalOrIndicatorData
    )

    # Needs, activites & gaps
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
    has_humanitarian_needs = models.BooleanField(default=False)
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

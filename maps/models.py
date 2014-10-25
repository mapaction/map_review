from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
"""
File name
Name of reviewer
Map title
Map language
GLIDE number
Disaster type
Disaster start date
Map production date
Situational data date
Day
Map extent
Map authors/producers
Donor
Map series indicator
Update frequency
Infographics

Disclaimer/indication of uncertainty
Copyright statement
Satellite data indicator
Phase type
Date of data
Name of sensor and source
Admin boundaries indicator
Most detailed data level
Source of data
Roads indicator
Source of data
Hydrographic network indicator
Source of data
Elevation data indicator
Type of data
Source of data
Settlement data indicator
Most detailed data level
Type of data
Source of data
Hospitals/health facilities indicator
Source of data
Schools indicator
Source of data
Shelter indicator
Source of data
Date of data
Geographic extent of impact indicator
Type of data
Are the data modelled/predicted or observed
Situational date
Damaged objects
Situational date
Population data indicator
Type of data
Source of data
Date of data
Affected population indicator
Humanitarian profile level 1 type
Disaggregated affected population type
Date of data
Source of data
Statistical data indicator
Statistical data type
Pre/post disaster indicator
Date of data
Source of data
Active clusters
Sub-cluster information indicator
Activity detail indicator
Assessments
Humanitarian needs indicator
Date of data
Source of data
Gaps
Resourcing/funding
Date of data
Source of data
Additional datasets
Data sources not directly associated with another dataset
"""


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
        help_text="Geographical extent of the map."
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
    series_indicator = models.BooleanField(
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

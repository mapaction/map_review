from django.contrib import admin

from .models import (
    Event, DataSource, StatisticalOrIndicatorData, Map, ReviewGroup
)

admin.site.register(Event)
admin.site.register(DataSource)
admin.site.register(StatisticalOrIndicatorData)
admin.site.register(Map)
admin.site.register(ReviewGroup)

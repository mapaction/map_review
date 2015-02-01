from django.contrib import admin

from .models import Actor, Event, DataSource, StatisticalOrIndicatorData, Map

admin.site.register(Actor)
admin.site.register(Event)
admin.site.register(DataSource)
admin.site.register(StatisticalOrIndicatorData)
admin.site.register(Map)

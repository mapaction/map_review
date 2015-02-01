# -*- coding: utf-8 -*-
from django.template.defaulttags import register
from django.db import models


@register.filter()
def obj_lookup(value, arg):
    """Incredibly lazy lookup..."""
    if not isinstance(arg, basestring):
        return None
    if not value:
        return None
    if isinstance(value, models.Model):
        attr = getattr(value, arg, None)
        if hasattr(attr, 'all'):
            attr.is_m2m = True
        if isinstance(attr, list):
            attr = {'all': attr, 'is_list': True}
        return attr
    if isinstance(value, dict):
        return value.get(arg, None)
    elif isinstance(value, list):
        try:
            return value[int(arg)]
        except (TypeError, IndexError):
            return None
    return None

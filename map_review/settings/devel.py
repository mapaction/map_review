#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import *
DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'map_review',
        'HOST': 'localhost'
    }
}

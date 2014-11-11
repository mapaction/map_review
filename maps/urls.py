# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^review/', views.CreateReview.as_view(), name="create_review"),
)

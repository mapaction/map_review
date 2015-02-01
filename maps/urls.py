# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.MapList.as_view(), name="maps_list"),
    url(r'^review/$', views.CreateReview.as_view(), name="create_review"),
    url(r'^review/(?P<group_slug>[-\w]+)/$',
        views.CreateGroupReview.as_view(), name="create_review"),
    url(r'^detail/(?P<pk>\d+)/', views.MapDetail.as_view(), name="maps_detail"),
)

# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from maps.models import ReviewGroup, Map


class IndexView(TemplateView):
    template_name = 'map_review/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['groups'] = ReviewGroup.objects.all()
        ctx['maps'] = Map.objects.order_by('-review_created_on')
        return ctx

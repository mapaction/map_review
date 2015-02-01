# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages
from django.utils.translation import ugettext as _

from .forms import CreateReviewForm
from .models import Map


class CreateReview(CreateView):
    """Basic creation of the Map Review."""
    form_class = CreateReviewForm
    template_name = 'maps/create.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Thanks for reviewing this map!')
        )
        return super(CreateReview, self).form_valid(form)


class MapList(ListView):
    """Basic list of maps."""
    template_name = 'maps/list.html'
    model = Map


class MapDetail(DetailView):
    """Basic detail view of a reviewed map"""
    template_name = 'maps/detail.html'
    model = Map

    def get_context_data(self, **kwargs):
        ctx = super(MapDetail, self).get_context_data(**kwargs)
        ctx['form'] = CreateReviewForm
        if 'reliefweb' in self.object.url:
            # TODO: we can use beautifulsoup or similer to get the img url?
            # Might be a bit cheeky...
            ctx['preview'] = "RELIEFWEB IMAGE HERE"
        return ctx

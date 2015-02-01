# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404

from .forms import CreateReviewForm
from .models import Map, ReviewGroup


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


class CreateGroupReview(CreateReview):
    """Review with group info set."""
    template_name = 'maps/group_create.html'

    @property
    def group(self):
        if not hasattr(self, '_group'):
            setattr(
                self,
                '_group',
                get_object_or_404(ReviewGroup, slug=self.kwargs['group_slug'])
            )
        return self._group

    def get_context_data(self, **kwargs):
        ctx = super(CreateGroupReview, self).get_context_data(**kwargs)
        ctx['group'] = self.group
        return ctx

    def get_form_kwargs(self):
        kwargs = super(CreateGroupReview, self).get_form_kwargs()
        initial = kwargs.get('initial', {})
        initial['event'] = self.group.event
        kwargs['initial'] = initial
        kwargs['group'] = self.group
        return kwargs

    def post(self, *args, **kwargs):
        # We disable the field which means it is not sent in the POST, so set it back
        self.request.POST['event'] = self.group.event.id
        return super(CreateGroupReview, self).post(*args, **kwargs)


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

# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView

from . forms import CreateReviewForm


class CreateReview(CreateView):
    """Basic creation of the Map Review."""
    form_class = CreateReviewForm
    template_name = 'maps/create.html'

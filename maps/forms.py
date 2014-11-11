# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper

from .models import Map


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Map

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

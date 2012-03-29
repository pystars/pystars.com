# -*- coding: utf-8 -*-
from django.views.generic import DetailView

from pystars.apps.profiles.models import Profile


class ProfileDetailView(DetailView):
    object = Profile

    def get_object(self, queryset=None):
        super(ProfileDetailView, self).get_object(self)
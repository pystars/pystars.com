# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import DetailView

from pystars.apps.profiles.models import Profile


class ProfileDetailView(DetailView):
    object = Profile

    def get_object(self, queryset=None):
        try:
            return Profile.objects.get(username=self.kwargs.get('username'))
        except ObjectDoesNotExist:
            raise Http404
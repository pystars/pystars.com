# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from pystars.apps.profiles.models import Profile

def profile(request):
    try:
        profile = request.user
    except (AttributeError, ObjectDoesNotExist):
        profile = {}

    return {
        'request': {'profile': profile}
    }
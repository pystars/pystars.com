# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader, Context

def profile(request):
    try:
        profile = request.user.profile
    except (AttributeError, ObjectDoesNotExist):
        profile = {}

    return {
        'profile': profile,
    }
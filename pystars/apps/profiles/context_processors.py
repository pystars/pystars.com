# -*- coding: utf-8 -*-
from django.template import loader, Context

def profile(request):
    try:
        profile = request.user.profile
    except AttributeError:
        profile = {}

    return {
        'profile': profile,
    }
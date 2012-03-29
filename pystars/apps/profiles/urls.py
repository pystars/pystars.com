# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from pystars.apps.profiles.views import ProfileDetailView

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/$',
        ProfileDetailView.as_view(),
        name='profile_detail_by_username',
    ),
)

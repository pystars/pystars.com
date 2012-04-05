# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from pystars.apps.main.views import IndexArticlesListView

urlpatterns = patterns('',
    url(r'^$', IndexArticlesListView.as_view(),
        name='index',
    ),
)
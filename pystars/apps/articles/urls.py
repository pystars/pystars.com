# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from pystars.apps.articles.views import CreateArticleView, \
    ArticleDetailView, ArticleEditView

urlpatterns = patterns('',
    url(r'^new/$',
        login_required(CreateArticleView.as_view()),
        name='create_article'
    ),
    url(r'^(?P<pk>\d+)/$',
        ArticleDetailView.as_view(),
        name='detail_article'
    ),
    url(r'^(?P<pk>\d+)/edit/$',
        login_required(ArticleEditView.as_view()),
        name='edit_article'
    ),
)
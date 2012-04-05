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
)
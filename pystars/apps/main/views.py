# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic.list import ListView
from pystars.apps.articles.models import Article

class IndexArticlesListView(ListView):
    model = Article

    def get_queryset(self):
        return self.model.objects.all()
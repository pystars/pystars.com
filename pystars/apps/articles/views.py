# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView
from pystars.apps.articles.forms import CreateArticleForm, EditArticleForm
from pystars.apps.articles.models import Article

from postmarkup import render_bbcode

class CreateArticleView(CreateView):
    model = Article
    form_class = CreateArticleForm

#    def get_form_kwargs(self, **kwargs):
#        kwargs = super(CreateArticleView, self).get_form_kwargs(**kwargs)
#        kwargs['initial']['author'] = self.request.user
#        return kwargs

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user

        instance.rendered_text = render_bbcode(form.cleaned_data['text'])

        instance.save()
        return redirect(reverse('detail_article', args=[instance.id]))


class ArticleDetailView(DetailView):
    model = Article


class ArticleEditView(UpdateView):
    model = Article
    form_class = EditArticleForm

    def get_object(self, queryset=None):
        object = super(ArticleEditView, self).get_object(queryset=queryset)
        if object.author == self.request.user:
            return object
        else:
            raise HttpResponseNotAllowed()

    def get_success_url(self):
        return reverse('detail_article', args=[self.kwargs['pk']])
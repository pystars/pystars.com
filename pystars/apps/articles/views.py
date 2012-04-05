# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from tagging.models import TaggedItem, Tag

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

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.rendered_text = render_bbcode(form.cleaned_data['text'])
        instance.save()
        return redirect(reverse('detail_article', args=[instance.id]))

    def get_success_url(self):
        return reverse('detail_article', args=[self.kwargs['pk']])


class TaggedListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        ctx = super(TaggedListView, self).get_context_data(**kwargs)
        ctx.update({'tag': self.kwargs['tag']})
        return ctx

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs['tag'])
        return TaggedItem.objects.get_by_model(self.model, tag)
# -*- coding: utf-8 -*-
from django import forms

from markitup.widgets import MarkItUpWidget
from pystars.apps.articles.models import Article

class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            'title',
            'text',
            'tags',
            'category',
            'is_draft',
        )


class EditArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            'title',
            'text',
            'tags',
            'category',
            'is_draft',
            )
# -*- coding: utf-8 -*-
import reversion
from django.db import models
from tagging.fields import TagField
from tagging.models import Tag

from pystars.apps.profiles.models import Profile

class Category(models.Model):
    title = models.CharField(u'Название', max_length=255,
        blank=False, null=False, unique=True)


class Article(models.Model):
    title = models.CharField(u'Заголовок', max_length=255,
        blank=False, null=False)
    text = models.TextField(u'Текст')
    rendered_text = models.TextField(u'HTML Текст')
    tags = TagField()

    author = models.ForeignKey(Profile, verbose_name=u'Автор')
    category = models.ForeignKey(Category, verbose_name=u'Раздел')
    is_draft = models.BooleanField(u'Черновик', default=False)
    created_at = models.DateTimeField(u'Дата добавления', auto_now_add=True)
    last_modified = models.DateTimeField(u'Последнее обновление', auto_now=True)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)

reversion.register(Article)
# -*- coding: utf-8 -*-
import postmarkup
from django import template

register = template.Library()

@register.filter
def bbtohtml(value):
    return postmarkup.render_bbcode(value)
# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, UserManager

class Profile(User):
    website = models.URLField(u'Страничка', blank=True, null=True)

    objects = UserManager()

    def __unicode__(self):
        return self.username

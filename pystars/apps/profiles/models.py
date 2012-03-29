# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, UserManager

class Profile(User):
    user_manager = UserManager()

    def __unicode__(self):
        return self.username

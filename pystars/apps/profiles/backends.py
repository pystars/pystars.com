# -*- coding: utf-8 -*-
from pystars.apps.profiles.models import Profile

class ProfileAuthenticationBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            profile = Profile.objects.get(username=username)
            if profile.check_password(password):
                return profile
        except Profile.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None

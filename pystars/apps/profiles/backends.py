# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from registration import signals
from registration.forms import RegistrationForm

from pystars.apps.profiles.models import Profile, RegistrationProfile

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


class RegistrationBackend(object):
    def register(self, request, **kwargs):
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
            password, site)
        signals.user_registered.send(sender=self.__class__,
            user=new_user,
            request=request)
        return new_user

    def activate(self, request, activation_key):
        activated = RegistrationProfile.objects.activate_user(activation_key)
        if activated:
            signals.user_activated.send(sender=self.__class__,
                user=activated,
                request=request)
        return activated

    def registration_allowed(self, request):
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_form_class(self, request):
        return RegistrationForm

    def post_registration_redirect(self, request, user):
        return ('registration_complete', (), {})

    def post_activation_redirect(self, request, user):
        return ('registration_activation_complete', (), {})

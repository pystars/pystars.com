# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate

from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy

from pystars.apps.profiles.models import Profile

class LoginForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username:
            try:
                Profile.objects.get(username=username)
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    u'''Неправильный логин или пароль.'''
                )

        if username and password:
            self.user_cache = authenticate(username=username,
                password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data
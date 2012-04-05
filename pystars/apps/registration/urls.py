# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from registration.views import activate, register
from registration.forms import RegistrationFormUniqueEmail
from pystars.apps.profiles.forms import LoginForm

urlpatterns = patterns('',
    # url(r'', include('social_auth.urls')),
    
    url(r'^register/$', 'registration.views.register',
            {'backend': 'pystars.apps.registration.backends.RegistrationBackend',
             'form_class': RegistrationFormUniqueEmail, },
        name='registration_register'),
    url(r'^activate/complete/$',
        direct_to_template,
            {'template': 'registration/activation_complete.html'},
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$',
        activate,
            {'backend': 'pystars.apps.registration.backends.RegistrationBackend'},
        name='registration_activate'),
    url(r'^register/$',
        register,
            {'backend': 'pystars.apps.registration.backends.RegistrationBackend'},
        name='registration_register'),
    url(r'^register/complete/$',
        direct_to_template,
            {'template': 'registration/registration_complete.html'},
        name='registration_complete'),
    url(r'^register/closed/$',
        direct_to_template,
            {'template': 'registration/registration_closed.html'},
        name='registration_disallowed'),
    url(r'^login/$',
        auth_views.login,
            {'template_name': 'registration/login.html',
             'authentication_form': LoginForm},
        name='auth_login'),

    (r'', include('registration.auth_urls')),
)

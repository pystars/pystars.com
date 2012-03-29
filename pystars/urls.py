from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pystars.views.home', name='home'),
    # url(r'^pystars/', include('pystars.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('pystars.apps.main.urls')),

    # Accounts
    url(r'^accounts/register/$', 'registration.views.register',
            {'backend': 'pystars.apps.profiles.backends.RegistrationBackend',
             'form_class': RegistrationFormUniqueEmail, },
        name='registration_register'),
    url(r'^accounts/', include('pystars.apps.profiles.urls')),
)

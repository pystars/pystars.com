from django.conf.urls import patterns, include, url

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

    url(r'^login_redirect_url/',
        'pystars.apps.main.views.login_redirect_handler',
        name='login_redirect_handler'
    ),
    # Accounts. Registration, activation etc.
    url(r'^accounts/', include('pystars.apps.registration.urls')),
    # Profiles.
    url(r'^profiles/', include('pystars.apps.profiles.urls')),
)

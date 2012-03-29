# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden

def login_redirect_handler(request):
    if (request.method == 'GET'):
        referer = request.META.get('HTTP_REFERER', None)
        if referer:
            return HttpResponseRedirect(referer)
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseForbidden()
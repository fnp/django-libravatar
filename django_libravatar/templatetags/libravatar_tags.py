# -*- coding: utf-8 -*-
# This file is part of django-libravatar, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.core.cache import cache
from django import template
from libravatar import libravatar_url
from django_libravatar.settings import LIBRAVATAR_DEFAULT, LIBRAVATAR_DEFAULT_HTTPS

register = template.Library()

@register.simple_tag(takes_context=True)
def libravatar(context, email, size=None):
    https = context['request'].is_secure()
    default = LIBRAVATAR_DEFAULT_HTTPS if https else LIBRAVATAR_DEFAULT_HTTP
    if hasattr(default, '__call__'):
        default = default(size)
    if not email:
        return default
    cache_key = "%s:%d:%d" % (email, size, https)
    print cache_key
    url = cache.get(cache_key)
    if url is None:
        print 'fetching...'
        url = libravatar_url(email,
            https=https,
            default=default,
            size=size)
        cache.set(cache_key, url, 60 * 60)
    return url

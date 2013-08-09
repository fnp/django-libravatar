# -*- coding: utf-8 -*-
# This file is part of django-libravatar, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.conf import settings

LIBRAVATAR_DEFAULT = getattr(settings, 'LIBRAVATAR_DEFAULT',
    lambda size: "https://seccdn.libravatar.org/nobody/%d.png" % size)
LIBRAVATAR_DEFAULT_HTTPS = getattr(settings, 'LIBRAVATAR_DEFAULT', LIBRAVATAR_DEFAULT)

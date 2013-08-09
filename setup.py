#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of django-libravatar, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
import os.path
from setuptools import setup, find_packages
from django_libravatar import __version__

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-libravatar',
    version=__version__,
    author='Radek Czajka',
    author_email='radekczajka@nowoczesnapolska.org.pl',
    url = 'http://git.nowoczesnapolska.org.pl/?p=django-libravatar.git',
    packages=find_packages(),
    include_package_data=True,
    license='GNU AGPL 3.0',
    description='Simple app for displaying Libravatars.',
    long_description=README,
    install_requires=[
        'django', 
        'pyLibravatar', 
        'pyDNS',
    ],

)

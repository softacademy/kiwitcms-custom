# -*- coding: utf-8 -*-

import os.path
from importlib import import_module

import pkg_resources
from django.contrib.messages import constants as messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

import tcms

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~ Overwriting settings in common.py

# email host settings
EMAIL_HOST = 'softacad.bg'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'support@softacad.bg'
EMAIL_HOST_PASSWORD = 'Support*123'
DEFAULT_FROM_EMAIL = 'support@softacad.bg'
EMAIL_SUBJECT_PREFIX = '[Kiwi-TCMS SoftAcademy] '
# -*- coding: utf-8 -*-
"""
Django settings for murex project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
import os
import ldap
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
APPLICATION_NAME= "Murex"
APPLICATION_DESC= "Toner management"

from django.utils.translation import ugettext_lazy as _
LANGUAGE_CODE = 'es'
LANGUAGES = (
  ('es', _('Spanish')),
  ('en', _('English')),
)
USE_I18N = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e!y00g3a(%!+!7yr5)ese+fc==68t*%it$*b&axr=%hu*4c6x2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# LDAP Configuration ==============/
# LDAP server
LDAP_SERVER = 'ldap://host_ldap:port'

# Dn for entry
LDAP_DN = 'dc=domain,dc=edu,dc=ar'

# LDAP authentication
#LDAP_USER_NAME='username'
#LDAP_USER_PASS='password'

# Organizational Unit for Person
LDAP_PEOPLE = 'People'
LDAP_PEOPLE = 'Group'
# =================================/

# =================================\
# django ldap configuration

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


AUTH_LDAP_SERVER_URI = LDAP_SERVER

#AUTH_LDAP_BIND_DN = "cn=%s,%s" % ( LDAP_USER_NAME, LDAP_DN )
#AUTH_LDAP_BIND_PASSWORD = LDAP_USER_PASS

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=%s,%s" % (LDAP_PEOPLE,LDAP_DN),
                                   ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# =================================/


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'jquery',
    'jquery_ui',
    'bootstrap_ui',
    'bootstrap_themes',
    'app',
    'django.templatetags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'app.middleware.ForceLangMiddleware',
)

ROOT_URLCONF = 'murex.urls'

WSGI_APPLICATION = 'murex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'murex_db',
        'USER': 'murex_user',
        'PASSWORD': 'user',
        'PORT': '5432',        
        'HOST': 'localhost',
    },
    'murex_owner': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'murex_db',
        'USER': 'murex_owner',
        'PASSWORD': 'owner',
        'PORT': '5432',        
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
     BASE_DIR + '/locale', )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# set static path for production
#STATIC_ROOT = '/srv/murex/shared/static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/static/',
)
# If the user isn't logged in, redirect to
#LOGIN_URL = '/login/'

#LOGIN_REDIRECT_URL = '/app/login/'
LOGIN_URL='/login/'
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.defaults',
            ],
        },
    },
]

# nombre de la clase css usada como separador en listados
CSS_SEPARATOR_NAME = 'separator'

# nombre de la clase (boostrap) usado como separador de color
CSS_SEPARATOR_COLOR1 = 'info'
CSS_SEPARATOR_COLOR2 = 'warning'

# Numero de items por pagina para todos los listados
PAGINATE_BY_PAGE = 25


SUIT_CONFIG = {
    'ADMIN_NAME': _('title')
}

# =================================\
# django ldap configuration

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


AUTH_LDAP_SERVER_URI = LDAP_SERVER

#AUTH_LDAP_BIND_DN = "cn=%s,%s" % ( LDAP_USER_NAME, LDAP_DN )
#AUTH_LDAP_BIND_PASSWORD = LDAP_USER_PASS

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=%s,%s" % (LDAP_PEOPLE,LDAP_DN),
                                   ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# =================================/

# loggin querys in develompent
# if DEBUG:
#     import logging
#     l = logging.getLogger('django.db.backends')
#     l.setLevel(logging.DEBUG)
#     l.addHandler(logging.StreamHandler())
#     logging.basicConfig(
#         level = logging.DEBUG,
#         format = " %(levelname)s %(name)s: %(message)s",
#     )

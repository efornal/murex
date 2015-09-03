"""
Django settings for murex project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# set static path for production
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


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
)

ROOT_URLCONF = 'murex.urls'

WSGI_APPLICATION = 'murex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
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

TIME_ZONE = 'UTC'

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
     BASE_DIR + '/locale', )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/static/',
)
# If the user isn't logged in, redirect to
#LOGIN_URL = '/login/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

#LOGIN_REDIRECT_URL = '/app/login/'
LOGIN_URL='/login/'
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#SITE_ID = 1


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    "app.processor.states",
    "app.processor.providers",
    "app.processor.current_state",
    "app.processor.current_provider",
)




# nombre de la clase css usada como separador en listados
CSS_SEPARATOR_NAME = 'separator'

# nombre de la clase (boostrap) usado como separador de color
CSS_SEPARATOR_COLOR1 = 'info'
CSS_SEPARATOR_COLOR2 = 'warning'

# Numero de items por pagina para todos los listados
PAGINATE_BY_PAGE = 25



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

# Django settings for BATMobileApp project.

import os
import logging

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
UPLOADS_DIR = '%s/uploads' % PROJECT_DIR
PRIVATE_UPLOADS_DIR = '%s/private_uploads' % PROJECT_DIR

logging.warning(PROJECT_DIR)

ADMINS = (
    ('Madalin Oprea', 'madalinoprea@gmail.com'),
)
EMAIL_SUBJECT_PREFIX = '[Mobile Portal]'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mobile_portal',                      # Or path to database file if using sqlite3.
        'USER': 'mobile_portal',                      # Not used with sqlite3.
        'PASSWORD': 'junky4:byway',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Bucharest'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = '/opt/site/static/'
BUILDS_DIR = '/opt/site/static/builds/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jtnz(hj25-24^z7!8u81o1=if&(7u77_=4))am7!jxpzbo@(g+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'BATMobileApp.urls'

TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    '%s/src/templates' % PROJECT_DIR,
)

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    
    'djangoratings',
    
    'BATMobileApp.core',
    'BATMobileApp.codes',
    'BATMobileApp.api',
)

AUTH_PROFILE_MODULE = 'core.UserProfile'

try:
    from local_settings import *
except Exception, e:
    import logging
    logging.warning('exception while importing local_settings: %s' % e)
    

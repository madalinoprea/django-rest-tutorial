'''
Created on Aug 13, 2010

@author: mario
'''

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mobile_portal',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'dev',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#CACHE_BACKEND = 'locmem://'
# Mem cache is restarted when app is reloaded after a modification and sessions are cleared
CACHE_BACKEND = 'file:///var/tmp/django_cache'


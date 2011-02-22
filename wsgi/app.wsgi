import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'BATMobileApp.settings'

# Add external libs and app to PYTHONPATH
sys.path.append('/opt/site/externals')
sys.path.append('/opt/site/src')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

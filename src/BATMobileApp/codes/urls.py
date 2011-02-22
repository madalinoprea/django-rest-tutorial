'''
Created on Aug 14, 2010

@author: mario
'''

from django.conf.urls.defaults import url, patterns
import views

urlpatterns = patterns('',
    # /codes/download/some_imported_file.xls
    url(r'^download/(?P<path>.*)$', views.download_importer, name='codes-download-import'),
)
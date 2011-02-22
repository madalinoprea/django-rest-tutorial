'''
Created on Aug 13, 2010

@author: mario
'''

from django.conf.urls.defaults import url, patterns
import views

urlpatterns = patterns('',
    url(r'^file/(?P<path>.*)$', views.protected_file),
    url(r'^number/$', views.number),
    
    url(r'^test_template_decorator', views.test_template_decorator),
    url(r'^test_json_response', views.test_json_response),
)
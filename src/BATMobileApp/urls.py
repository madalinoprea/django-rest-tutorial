from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^core/', include('BATMobileApp.core.urls')),
    (r'^codes/', include('BATMobileApp.codes.urls')),
    
    (r'^api/', include('BATMobileApp.api.urls')),
    

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)

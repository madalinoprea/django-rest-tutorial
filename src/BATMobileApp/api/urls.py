'''
Created on Aug 13, 2010

@author: mario
'''

from django.conf.urls.defaults import url, patterns
from django.contrib.auth.decorators import login_required

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import generate_doc

from BATMobileApp.api.handlers import MobileApplicationHandler,\
    UserProfileHandler, RegisterDeviceHandler, ValidateCodeHandler,\
    VoteAppHandler
from org.mario.utils import render_to

import logging

ad = {'authentication': HttpBasicAuthentication(realm='Mobile Portal Realm')}

applications_handler = Resource(MobileApplicationHandler)
userprofile_handler = Resource(UserProfileHandler)
register_handler = Resource(RegisterDeviceHandler)
validate_handler = Resource(ValidateCodeHandler, **ad)
vote_app_handler = Resource(VoteAppHandler, **ad)

#@login_required
@render_to('api/docs.html')
def doc_view(request):
    '''
    Generates API's documentation for logged users.
    @param request:
    '''
    import sys
    module = sys.modules[__name__]
    docs = []
    logging.warning('Module %s' % module)
    for k, v in module.__dict__.items():
        if isinstance(v, Resource):
            doc = generate_doc(type(v.handler))
            logging.warning('Doc: %s' % doc.__dict__)
            docs.append(doc)
    
    return {'docs': docs}
    
urlpatterns = patterns('',
       url(r'^docs/$', doc_view),
       
       url(r'^apps/$', applications_handler),
       url(r'^app/(?P<app_id>\d+)/vote/(?P<score>\d{1})/$', vote_app_handler),
       
       url(r'^apps/(?P<name>[^/]+)/', applications_handler),
#       url(r'^apps/(?P<app_id>\d+)/$', vote_app_handler),
       
       url(r'^user/(?P<user>[^/]+)/$', userprofile_handler),
       url(r'^user/(?P<user>[^/]+)/register/$', register_handler),
       url(r'^user/(?P<user>[^/]+)/validate/(?P<code_number>\w+)/$', validate_handler),
)

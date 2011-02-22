'''
Created on Aug 13, 2010

@author: mario
'''

from piston.handler import BaseHandler
from BATMobileApp.core.models import MobileApplication, UserProfile
from piston.utils import rc
from django import forms
import logging

class MobileApplicationHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = MobileApplication
    
class UserProfileHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = UserProfile
    
class RegisterDeviceHandler(BaseHandler):
    allowed_methos = ('GET', )
    
    def read(self, request, user):
        return {'response': 'register device %s' % user}
    
class ValidateCodeHandler(BaseHandler):
    allowed_methods = ('GET', )
    
    def read(self, request, user, code):
        return {'response': 'device %s tries to validate code %s' % (user, code)}


class VoteAppHandler(BaseHandler):
    allowed_methods = ('GET')
    
    def read(self, request, app_id, score):
        logging.warning('Users %s rates app %s: %s' % (request.user, app_id, score))
        
        # request.user,
        try:
            app = MobileApplication.objects.get(id=app_id)
            app.rating.add(score=score, user=request.user, ip_address=request.META['REMOTE_ADDR'])
            app.save()
            
            return {'app': app}
        except Exception as e:
            return {'error': 'Cannot record vote: %s' % e}
    
    
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from BATMobileApp.core.models import MobileApplication
from django.core.cache import cache


class ServicesTest(TestCase):
    def setUp(self):
        cache.set('test_key', 100)
    
    def test_cache(self):
        result = cache.get('test_key')
        self.failUnless(result==100, 'Incorrect value read from cache.')

class SimpleTest(TestCase):
    
#    def testCreateMobileApp(self):
#        app = MobileApplication(name='Test', description='App description', cost=100)
#        app.save()
        
        # check if app was created
#        self.failIf(MobileApplication.objects.get(name='Test')==None, 'Cannot create mobile application')
        
        # TODO: Test to add builds to the app
    
    def testUserProfileCreation(self):
        pass
    


"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from BATMobileApp.codes.models import Code, CodeValidation, CodeImporter
from BATMobileApp.core.models import UserProfile
import logging

class CodeValidationTest(TestCase):
    
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user('mario', 'madalinoprea@gmail.com', 'the_password')
        # User with no profile created
        self.invalid_user = User.objects.create_user('second_user', 'user2@mail.com', 'user2')
        self.other_user = User.objects.create_user('other_user', 'otheruser@mail.com', 'other_user_pass')
        
        UserProfile.objects.create(user=self.user, platform='a', available_credits=1000)
        UserProfile.objects.create(user=self.other_user, platform='s', available_credits=2000)
        
        importer = CodeImporter.objects.create(file='test_codes.xls', user=self.user)
        Code.objects.create(code='TEST_AAAAA', credits=100, importer=importer)
        Code.objects.create(code='TEST_DISABLED_CODE', credits=200, importer=importer, is_enabled=False)
        Code.objects.create(code='TEST_USED_CODE', credits=300, importer=importer, is_used=True)
        
    def test_invalid_profile_validation(self):
        validation = CodeValidation.validate(self.invalid_user, 'TEST_AAAAA')
        self.failIf(validation.is_valid, True)
        self.failUnlessEqual(validation.details, "User %s doesn't have a registered profile" % self.invalid_user, 
                             'Unexpected details received when validating for invalid user')
    
    def test_valid_code(self):
        validation = CodeValidation.validate(self.user, 'TEST_AAAAA')
        self.failUnlessEqual(validation.is_valid, True)
        
        self.failUnless(self.user.get_profile().available_credits, 1100)
        self.failIf(validation.validated_code.is_used==False, 'Validated code was not marked as used.')
        
        # try to re-validate the code for the same user
        validation = CodeValidation.validate(self.user, 'TEST_AAAAA')
        self.failUnlessEqual(validation.is_valid, False)
        self.failUnless(self.user.get_profile().available_credits, 1100)
        
        # for another user
        validation = CodeValidation.validate(self.other_user, 'TEST_AAAAA')
        self.failIf(validation.is_valid, 'Already validated code was validated again.')
        self.failUnless(self.user.get_profile().available_credits, 2000) #user's credits were changed?
        
    def test_non_existent_code(self):
        validation = CodeValidation.validate(self.user, 'NOT_EXISTENT_CODE')
        self.failUnlessEqual(validation.is_valid, False, 'Validation was OK for an non existent code.')
        self.failUnlessEqual(validation.details, 'Inputed code is not enabled or is not present in the database.',
                             'Details for validation are not correct.')
    
    def test_disabled_code(self):
        validation = CodeValidation.validate(self.user, 'TEST_DISABLED_CODE')
        self.failIf(validation.is_valid, True)
        
    def test_used_code(self):
        validation = CodeValidation.validate(self.user, 'TEST_USED_CODE')
        self.failIf(validation.is_valid, True)
        self.failUnlessEqual(validation.details, 'Inputed code is already used.',
                             'Details for used code validation are incorrect.')


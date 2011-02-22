from django.db import models
from djangoratings.fields import RatingField
from django.contrib.auth.models import User

import random

class MobileApplication(models.Model):
    """(MobileApplication description)"""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cost = models.SmallIntegerField(help_text='Cost in credits')
    rating = RatingField(range=5)

    def average_rating(self):
        if self.rating.votes:
            return '%0.1d' % (self.rating.score / self.rating.votes)

    def __unicode__(self):
        return self.name

PLATFORM_CHOICES = (
                    ('a', 'Android'),
                    ('r', 'RIM'),
                    ('s', 'Symbian'),
                    ('w', 'Windows Mobile'),
                    )

class ApplicationBuild(models.Model):
    """(ApplicationBuild description)"""
    
    app = models.ForeignKey(MobileApplication)
    platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES)
    descriptor_file = models.FileField(upload_to="builds", blank=True)
    binary_file = models.FileField(upload_to="builds", blank=False)
    
    class Meta:
        unique_together = ( ('app', 'platform'), )

    def __unicode__(self):
        return u"ApplicationBuild"


class UserProfile(models.Model):
    """(UserProfile description)"""
    
    user = models.OneToOneField(User)
    available_credits = models.IntegerField(default=0)
    purchased_apps = models.ManyToManyField(MobileApplication, blank=True)
    platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES)
    
    # TODO: Complete token validation - when token expires, etc... 
    token = models.CharField(max_length=32, unique=True)
    
    def _random_token(self):
        random.seed()
        hash = random.getrandbits(128)
        return '%016x' % hash
    
    def available_apps(self):
        # retrieve the available builds for this platform
        builds = ApplicationBuild.objects.filter(platform=self.platform)
        app_ids = [build.app.pk for build in builds]
        purchased_ids = [app.pk for app in self.purchased_apps.all()]
        available_app_ids = filter(lambda id: id not in purchased_ids, app_ids)
        
        return MobileApplication.objects.filter(pk__in=available_app_ids)
    
    def save(self, force_insert=False, force_update=False, using=None):
        self.token = self._random_token()
        
        super(UserProfile, self).save(force_insert=False, force_update=False, using=None)
    

    def __unicode__(self):
        return u"%s" % (self.user.username)

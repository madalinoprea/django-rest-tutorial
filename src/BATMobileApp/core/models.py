from django.db import models

# Create your models here.

class MobileApplication(models.Model):
    """(MobileApplication description)"""
    
    

    def __unicode__(self):
        return u"MobileApplication"

PLATFORM_CHOICES = (
                    ('a', 'Android'),
                    ('r', 'RIM'),
                    (''))
class ApplicationBuild(models.Model):
    """(ApplicationBuild description)"""
    
    platform = models.CharField(max_length=1, choices=)

    def __unicode__(self):
        return u"ApplicationBuild"

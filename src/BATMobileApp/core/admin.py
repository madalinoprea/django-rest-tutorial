'''
Created on Aug 13, 2010

@author: mario
'''

from django.contrib import admin
from BATMobileApp.core.models import ApplicationBuild, MobileApplication,\
    UserProfile

class ApplicationBuildAdmin(admin.TabularInline):
    model = ApplicationBuild
    extra = 1

class MobileApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'average_rating', 'rating_votes', 'rating_score']
    search_fields = ['name', 'description',]
    inlines = [ApplicationBuildAdmin, ]
    
class UserProfileAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(MobileApplication, MobileApplicationAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

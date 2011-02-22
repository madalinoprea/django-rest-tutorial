'''
Created on Aug 14, 2010

@author: mario
'''

from django.contrib import admin
from django.contrib import messages 
from BATMobileApp.codes.models import CodeImporter, Code

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'credits', 'is_used', 'is_enabled')
    list_filter = ('is_used', 'is_enabled')
    readonly_fields = ('importer', )

class CodeImporterAdmin(admin.ModelAdmin):
    exclude = ('user', 'is_valid', )  # These fields are populated by save method with user who did the request and import result
    readonly_fields = ('import_results', )
    list_display = ('file', 'imported_at', 'user', 'is_valid')
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        else:
            messages.error(request, 'Imports already created cannot be edited.')
    
admin.site.register(Code, CodeAdmin)
admin.site.register(CodeImporter, CodeImporterAdmin)
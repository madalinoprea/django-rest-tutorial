from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import xlrd
import logging
from django.core.urlresolvers import reverse
from BATMobileApp.core.models import UserProfile

#code_imports_storage=FileSystemStorage(location=settings.PRIVATE_UPLOADS_DIR)
private_storage = FileSystemStorage(location=settings.PRIVATE_UPLOADS_DIR, 
                                  base_url='/codes/download/')

class Code(models.Model):
    """(Code description)"""
    
    code = models.CharField(unique=True, max_length=32)
    credits = models.IntegerField()
    is_used = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)
    importer = models.ForeignKey('CodeImporter')
    
    #TODO: Maybe - Add date range validity
    
    def __unicode__(self):
        return u"Code"


class CodeValidation(models.Model):
    """(CodeValidation description)"""
    
    user = models.ForeignKey(User)
    input_code = models.CharField(max_length=32)
    
    validated_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=False)
    details = models.TextField(blank=True, null=True)
    validated_code = models.OneToOneField(Code, blank=True, null=True)
    
    @staticmethod
    def validate(user, code_to_validate):
        code_validation = CodeValidation(user=user, input_code=code_to_validate)
        
        try:
            user_profile = user.get_profile()
        except UserProfile.DoesNotExist:
            user_profile = None
            
        if not user_profile:
            code_validation.is_valid = False
            code_validation.details = "User %s doesn't have a registered profile" % user
        else:
            try:
                code = Code.objects.filter(is_enabled=True).get(code=code_to_validate)
            except Code.DoesNotExist:
                code = None
            
            if not code:
                code_validation.is_valid = False
                code_validation.details = 'Inputed code is not enabled or is not present in the database.'
            elif code.is_used:
                code_validation.is_valid = False
                code_validation.details = 'Inputed code is already used.'
            else:
                code_validation.is_valid = True
                code_validation.validated_code = code
                
                code.is_used = True
                user_profile.available_credits += code.credits
                code.save()
                user_profile.save()
        
        code_validation.save()
        return code_validation
            
    def __unicode__(self):
        return u"CodeValidation"
    
class CodeImporter(models.Model):
    """(CodeImporter description)"""
    
    file = models.FileField(upload_to='code_importes', storage=private_storage)
    user = models.ForeignKey(User)
    imported_at = models.DateTimeField(blank=True, auto_now_add=True)
    is_valid = models.BooleanField(default=False)
    import_results = models.TextField()
    
    # Options
#    skip_already_imported = models.BooleanField(default=False, help_text='If checked, it will continue')

    class Meta:
        permissions = (
            ('can_download_imports', 'Can download imported code files.'),
            )
    
    def __unicode__(self):
        return u"CodeImporter: %s" % self.file

    def _importXls(self):
        # Import codes from file
        logging.info('%s imports codes from file %s' % (self.user, self.file))
        errors = []
        n_codes_imported = 0
        try:
            book = xlrd.open_workbook(self.file.path)
            sheet = book.sheet_by_index(0)
            
            for row in range(1, sheet.nrows):
                code = sheet.cell_value(row, 1)
                credits = sheet.cell_value(row, 2)
                
                logging.warning('row %d: %s %s' % (row, code, credits))
                
                # Create Code object and save it
                try: 
                    obj = Code(code=code, credits=credits, importer=self)
                    obj.save()
                    n_codes_imported += 1
                    logging.debug('Save code..')
                except Exception as exception:
                    errors.append('Cannot save code %s, %s (file %s, row %d): %s' % (code, credits, self.file, row, exception))
        except Exception as exception:
            errors.append('Import error %s: %s' % (self.file, exception))
        
        self.import_results = '\r\n'.join(errors)
        self.import_results = 'Imported codes: %s\r\n\r\n%s' % (n_codes_imported, self.import_results)
        self.is_valid = False if len(errors) else True
        
        # call parent save to save the results of import
        super(CodeImporter, self).save()
        
    
    def save(self, force_insert=False, force_update=False, using=None):
        if not force_update:
            super(CodeImporter, self).save(force_insert, force_update, using)
            self._importXls()
        

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.views.static import serve
from django.conf import settings
import logging

@permission_required('codes.can_download_imports')
@login_required
def download_importer(request, path):
    logging.warning('Serving import file: %s' % path)
    return serve(request, path, document_root=settings.PRIVATE_UPLOADS_DIR)

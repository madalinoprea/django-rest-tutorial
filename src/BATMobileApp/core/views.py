# Create your views here.
from django.conf import settings
from django.views.static import serve
import logging
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from org.mario.utils import render_to, json_view

@login_required
def protected_file(request, path):
    #FIXME check if access allowed
    logging.warning('Serving file: %s' % path)
    
    return serve(request, path, document_root=settings.BUILDS_DIR)

def number(request):
    return HttpResponse('A number')

@render_to('test_template_decorator.html')
def test_template_decorator(request):
    return {'name': 'mario', 'credits': 1000}

@json_view
def test_json_response(request):
    return {'name': 'mario', 'credits': 1220}
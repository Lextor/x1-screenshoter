from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from x1scr.apps.program.models import Program, Features


def download(request):
    download_program = Program.objects.filter(published=1)
    return render_to_response('download.html',
                              context_instance=RequestContext(request, {'download_program': download_program}))


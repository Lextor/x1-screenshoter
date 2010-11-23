from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.http import HttpResponseRedirect, HttpResponse
#from datetime import datetime
from x1scr.apps.program.models import Program


def download(request):
    programs = Program.objects.filter(published=True)
    return render_to_response('download.html',
                              context_instance=RequestContext(request,
                                                              dict(programs=programs)))

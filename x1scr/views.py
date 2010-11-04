
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request, dict()))


def base(request):
    return render_to_response('base.html',
                              context_instance=RequestContext(request, dict()))

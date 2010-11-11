
#from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.flatpages.models import FlatPage


def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request, dict()))


def base(request):
    return render_to_response('base.html',
                              context_instance=RequestContext(request, dict()))


def about(request):
    url_path = request.META['PATH_INFO']
    flatpage = get_object_or_404(FlatPage, url=url_path)
    return render_to_response('flatpages/about.html',
                              context_instance=RequestContext(request, dict(flatpage=flatpage)))
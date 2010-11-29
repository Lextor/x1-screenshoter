
#from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.flatpages.models import FlatPage
from x1scr.apps.screenshot.models import ScreenshotFile
from x1scr.apps.news.models import News


def index(request):
    url_path = request.META['PATH_INFO']
    flatpage = get_object_or_404(FlatPage, url=url_path)
    return render_to_response('index.html',
                              context_instance=RequestContext(request, dict(flatpage=flatpage)))


def base(request):
    return render_to_response('base.html',
                              context_instance=RequestContext(request, {'news': news}))


def about(request):
    url_path = request.META['PATH_INFO']
    flatpage = get_object_or_404(FlatPage, url=url_path)
    return render_to_response('flatpages/about.html',
                              context_instance=RequestContext(request, dict(flatpage=flatpage)))


def features(request):
    url_path = request.META['PATH_INFO']
    flatpage = get_object_or_404(FlatPage, url=url_path)
    return render_to_response('flatpages/about.html',
                              context_instance=RequestContext(request, dict(flatpage=flatpage)))


def termsofuse(request):
    url_path = request.META['PATH_INFO']
    flatpage = get_object_or_404(FlatPage, url=url_path)
    return render_to_response('flatpages/about.html',
                              context_instance=RequestContext(request, dict(flatpage=flatpage)))


def message(request):
    return render_to_response('message.html',
                              context_instance=RequestContext(request, dict()))


def profile(request):
    my_screenshots = ScreenshotFile.objects.filter(user=request.user)
    return render_to_response('profile.html',
                              context_instance=RequestContext(request, {'my_screenshots': my_screenshots}))


def news(request):
    news = News.objects.filter(published=1).order_by('-date_published')[0:3]
    return render_to_response('news.html',
                              context_instance=RequestContext(request, {'news': news}))


def news_item(request, news_id):
    news = News.objects.get(pk=news_id)
    return render_to_response('news_item.html',
                              context_instance=RequestContext(request, {'news': news}))

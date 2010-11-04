from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django import forms
from django.conf import settings

from x1scr.apps.screenshot.models import ScreenshotFile


class TestFileSenderForm(forms.Form):
    file_screenshot = forms.ImageField()


def test_file_sender_form(request):
    form = TestFileSenderForm()
    return render_to_response('screenshot/test_file_sender_form.html',
                              context_instance=RequestContext(request,
                                                              dict(form=form)))


def file_uploader(request):
    print request.POST, request.FILES
    if request.method == "POST" and \
    'file_screenshot' in request.FILES and \
    request.FILES['file_screenshot']:
        file_object = request.FILES['file_screenshot']
        screenshot_instance = ScreenshotFile(name=file_object.name, user=request.user)
        screenshot_instance.screenshot.save(file_object.name, file_object, save=True)
        return HttpResponse(settings.SITE_URL + screenshot_instance.screenshot.url)

    return redirect('test-sender-file')


def file_conteiner(request, hash_key):
    return HttpResponse('file will be here')

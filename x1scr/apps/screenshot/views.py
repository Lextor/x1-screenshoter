import os

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django import forms
from django.conf import settings


class TestFileSenderForm(forms.Form):
    file_screenshot = forms.ImageField()


def handle_uploaded_file(f):
    destination = open('some/file/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


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
        file_name = os.path.join(settings.SCREENSHOT_ROOT, file_object.name)
        destination = open(file_name, 'wb+')
        destination.write(file_object.read())
        destination.close()
        return HttpResponse(settings.SITE_URL + settings.MEDIA_URL + 'screenshots/' + file_object.name)

    return redirect('test-sender-file')

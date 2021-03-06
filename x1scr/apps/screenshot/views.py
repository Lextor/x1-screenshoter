from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django import forms
import xml.etree.ElementTree as ET
from bitly import bitly

#from x1scr.utils.thumbs import generate_thumb
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
    if request.method == "POST" and \
    'file_screenshot' in request.FILES and \
    request.FILES['file_screenshot']:
        file_object = request.FILES['file_screenshot']
        screenshot_instance = ScreenshotFile(name=file_object.name)
        if request.user.is_authenticated():
            screenshot_instance.user = request.user
        screenshot_instance.screenshot.save(file_object.name, file_object, save=True)
        
        api = bitly.Api(login=settings.BIT_USERNAME, apikey=settings.API_KEY)
        long_url = screenshot_instance.hash_url()    
        short_url=api.shorten(long_url)
        screenshot_instance.short_url = short_url
        screenshot_instance.save()
        
        root_tree = ET.Element("xscreenshot")
        errorid = ET.SubElement(root_tree, "errorid")
        directlink = ET.SubElement(root_tree, "directlink")
        directlink.text = screenshot_instance.hash_url()
        forumlink = ET.SubElement(root_tree, "forumlink")
        bloglink = ET.SubElement(root_tree, "bloglink")
        shortlink = ET.SubElement(root_tree, "shortlink")
        shortlink.text = short_url

        return HttpResponse(ET.tostring(root_tree), mimetype="text/xml")

    return redirect('test-sender-file')


def file_conteiner(request, hash_key):
    screenshot_file = get_object_or_404(ScreenshotFile, unique_hash=hash_key)
    short_url = screenshot_file.short_url
    return render_to_response('screenshot/screenshot_container.html',
                              context_instance=RequestContext(request,
                                                              dict(screenshot_file=screenshot_file,
                                                                   short_url=short_url)))

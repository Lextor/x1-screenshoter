from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from x1scr.apps.inbox.models import ContactForm, ContactLog


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            now_date = datetime.now()
            Contact_object = ContactLog(email=cleaned_data['email'],
                                        name=cleaned_data['name'],
                                        subject=cleaned_data['subject'],
                                        text=cleaned_data['text'],
                                        timestamp=now_date)
            Contact_object.save()

            return HttpResponseRedirect('/message/')
    else:
        form = ContactForm()

    return render_to_response('contact.html', {},
                            context_instance=RequestContext(request, {'form': form}))

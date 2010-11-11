from django.shortcuts import render_to_response
from django.template import RequestContext
from x1scr.apps.inbox.models import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render_to_response('contact.html', {},
                            context_instance=RequestContext(request, {'form': form}))



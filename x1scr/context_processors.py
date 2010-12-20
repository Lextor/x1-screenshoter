from django.conf import settings
from x1scr.apps.navigation.models import Navigation

def media_url(request):
    return {'MEDIA_PREFIX': '/' + settings.MEDIA_URL}
    
def navigation(request):
    navigation = Navigation.objects.filter(published=1).order_by('order')
    return {'navigation': navigation}


from django.conf import settings


def media_url(request):
    return {'MEDIA_PREFIX': '/' + settings.MEDIA_URL}

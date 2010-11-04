from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "x1scr.views.index", name="index"),
    url(r'^base/$', "x1scr.views.base", name="base"),
    (r'^screenshot/', include("x1scr.apps.screenshot.urls")),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEV_MODE:
    urlpatterns += patterns('',
        (r'^%s(.*)$' % settings.MEDIA_URL,
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

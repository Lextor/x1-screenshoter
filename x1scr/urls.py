from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from forms import SuperCaptchaForm

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "x1scr.views.index", name="index"),    
    url(r'^download/$', "x1scr.apps.program.views.download", name="download"),    
    url(r'^contact/$', "x1scr.apps.inbox.views.contact", name="contact"),
    url(r'^message/$', "x1scr.views.message", name="message"),
    url(r'^base/$', "x1scr.views.base", name="base"),
    (r'^screenshot/', include("x1scr.apps.screenshot.urls")),
    url(r'^captcha/(?P<code>[\da-f]{32})/$', 'supercaptcha.draw'),
    (r'^accounts/register/$', 'registration.views.register', {'form_class': SuperCaptchaForm, 'backend': 'registration.backends.default.DefaultBackend'}),
    (r'^accounts/', include('registration.urls')),
    (r'^profiles/', include('profiles.urls')),        
    url(r'^news/(?P<news_id>\d+)$', "x1scr.views.news_item", name="news_item"),
    url(r'^accounts/profile/$', "x1scr.views.profile", name="profile"),
    (r'^openid/', include('django_openid_auth.urls')),       
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEV_MODE:
    urlpatterns += patterns('',
        (r'^%s(.*)$' % settings.MEDIA_URL,
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
        (r'^(favicon.ico)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

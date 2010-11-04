from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('x1scr.apps.screenshot.views',
    url(r'^send_file/$', "test_file_sender_form", name="test-sender-file"),
    url(r'^file_upload/$', "file_uploader", name="file-uploader"),
    url(r'^(?P<hash_key>.+)$', "file_conteiner", name="file-conteiner"),
)

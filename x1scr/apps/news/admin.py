from django.contrib import admin
from django.conf import settings
from x1scr.apps.news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'chortext', 'publisher', 'published', 'date_published')
    search_fields = ['name']
    list_filter = ['publisher', 'published', 'date_published']
    date_hierarchy = 'date_published'

    class Media:
        js = ('/%sjs/tiny_mce/tiny_mce.js' % settings.MEDIA_URL,
              '/%sjs/textareas.js' % settings.MEDIA_URL, )

admin.site.register(News, NewsAdmin)

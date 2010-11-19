from django.contrib import admin
from x1scr.apps.inbox.models import ContactLog,  UserProfile
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.conf import settings


class ContactLogAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subject', 'timestamp')
    search_fields = ['email']
    list_filter = ['timestamp']
    date_hierarchy = 'timestamp'
    fieldsets = (
        (None, {
            'fields': ('email', 'name', 'subject', 'text')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('timestamp', 'comment')
        }),
        )


class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('/%sjs/tiny_mce/tiny_mce.js' % settings.MEDIA_URL,
              '/%sjs/textareas.js' % settings.MEDIA_URL,)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(ContactLog, ContactLogAdmin)
admin.site.register(UserProfile)

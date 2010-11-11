from django.contrib import admin
from x1scr.apps.inbox.models import ContactFile


class ContactFileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subject', 'timestamp')
    search_fields = ['email']
    list_filter = ['timestamp']
    fieldsets = (
        (None, {
            'fields': ('email', 'name', 'subject', 'text')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('timestamp', 'comment')
        }),
        )


admin.site.register(ContactFile, ContactFileAdmin)

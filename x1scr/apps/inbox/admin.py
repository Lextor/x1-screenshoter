from django.contrib import admin
from x1scr.apps.inbox.models import ContactLog


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


admin.site.register(ContactLog, ContactLogAdmin)
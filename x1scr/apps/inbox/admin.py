from django.contrib import admin
from x1scr.apps.inbox.models import ContactFile


class ContactFileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subject', 'timestamp')
    search_fields = ['email']    
    fieldsets = (
        (None, {
            'fields': ('vname', 'vcode', 'xtcdescription', 'xtclasstype', 'class_order')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('nshablon', 'xtcconst')
        }),
        )


admin.site.register(ContactFile, ContactFileAdmin)

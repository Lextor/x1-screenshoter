
from django.contrib import admin
from x1scr.apps.program.models import Program, Features


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('version', 'platform', 'releasedate', 'published')
    search_fields = ['description', 'platform']
    list_filter = ['platform', 'published', 'version', 'releasedate']
    date_hierarchy = 'releasedate'


admin.site.register(Program, ProgramAdmin)
admin.site.register(Features)

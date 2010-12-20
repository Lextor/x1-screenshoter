from django.contrib import admin
from x1scr.apps.navigation.models import Navigation


class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    search_fields = ['name']
    list_filter = ['published']
    

    
admin.site.register(Navigation, NavigationAdmin)

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/textareas.js',)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

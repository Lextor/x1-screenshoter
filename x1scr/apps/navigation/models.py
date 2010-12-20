from django.db import models
from django.contrib.flatpages.models import FlatPage

class Navigation(models.Model):
    name = models.CharField(max_length=30)
    flatpage = models.ForeignKey(FlatPage, blank=True)
    static_url = models.CharField(max_length=255, 
                                  help_text="Example: '/url/'. Make sure to have leading and trailing slashes.")
    order = models.IntegerField(null=True)
    published = models.BooleanField(default=False)
    

    def __unicode__(self):
        return self.name

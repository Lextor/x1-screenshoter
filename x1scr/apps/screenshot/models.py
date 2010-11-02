import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class ScreenshotFile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    screenshot = models.ImageField(upload_to='screenshots', max_length=384)
    unique_hash = models.CharField(unique=True, max_length=8, editable=False)
    name = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return settings.SITE_URL + self.screenshot.url

    def save(self, *args, **kwargs):
        '''
        on first save generate random hash key
        '''
        if self.pk is None:
            while True:
                random_hash = os.urandom(8).encode('hex')
                if ScreenshotFile.objects.filter(unique_hash=random_hash).count() == 0:
                    break
            self.unique_hash = random_hash
        super(ScreenshotFile, self).save(*args, **kwargs)

    def hash_url(self):
        """
        return unical link with hash key
        """
        return ''

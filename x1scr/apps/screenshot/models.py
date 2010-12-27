import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from x1scr.utils.thumbs import ImageWithThumbsField


class ScreenshotFile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    screenshot = ImageWithThumbsField(upload_to='screenshots', max_length=384, sizes=((100, 100), ), storage='storages.backends.s3.S3Storage')    
    unique_hash = models.CharField(unique=True, max_length=16, editable=False)
    name = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(max_length=256)

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
        return unical link with hash key to container page with image
        """
        return settings.SITE_URL[:-1] + reverse('file-conteiner', args=[self.unique_hash])

    def direct_url(self):
        '''
        return direct url for access to file
        '''
        return self.screenshot.url

    def get_thumbnail_url(self):
        return self.screenshot.url_100x100     
    

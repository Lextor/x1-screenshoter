from django.db import models
from x1scr.utils.thumbs import ImageWithThumbsField


class Features(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField() 
    image = models.ImageField(upload_to='programs')  

    def __unicode__(self):
        return self.name


class Program(models.Model):
    version = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)
    description = models.TextField()
    features = models.ManyToManyField(Features)
    ico = ImageWithThumbsField(upload_to='programs', sizes=((30, 30), ))
    program_file = models.FileField(upload_to='programs')
    releasedate = models.DateField(blank=True)
    promo = models.TextField(blank=True)
    published = models.BooleanField()

    def __unicode__(self):
        return self.version

    def get_ico_url(self):
        return self.ico.url_30x30

    def get_program_file_url(self):
        return self.program_file.url





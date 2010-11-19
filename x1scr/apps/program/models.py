from django.db import models


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
    ico = models.ImageField(upload_to='programs') 
    releasedate = models.DateField()
    promo = models.TextField(blank=True)
    program_file = models.FileField(upload_to='programs')
    published = models.BooleanField()

    def __unicode__(self):
        return self.version




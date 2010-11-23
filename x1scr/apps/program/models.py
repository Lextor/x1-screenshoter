from django.db import models


class Features(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='programs/features')

    def __unicode__(self):
        return self.name


class Program(models.Model):
    version = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)
    description = models.TextField()
    features = models.ManyToManyField(Features, null=True, blank=True)
    ico = models.ImageField(upload_to='programs', null=True, blank=True)
    releasedate = models.DateField()
    promo = models.TextField(blank=True)
    program_file = models.URLField()
    published = models.BooleanField()

    def __unicode__(self):
        return "%s-%s" % (self.platform, self.version)

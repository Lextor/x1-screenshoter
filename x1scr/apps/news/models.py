from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    chortext = models.TextField()
    text = models.TextField()
    publisher = models.ForeignKey(User)
    published = models.BooleanField()
    date_published = models.DateField()

    def __unicode__(self):
        return self.title

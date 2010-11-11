from django.db import models
import datetime


class ContactFile(models.Model):
    email = models.EmailField(max_length=75)
    name = models.CharField(blank=True, max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateField(auto_now_add=False)
    comment = models.TextField(blank=True)

    def __unicode__(self):
        return self.email

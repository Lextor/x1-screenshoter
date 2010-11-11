from django.db import models


class ContactFile(models.Model):
    email = models.
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.
    comment = models.TextField()
    
    def __unicode__(self):
        return self.email

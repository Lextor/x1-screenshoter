from django.db import models
from django.forms import ModelForm


class ContactLog(models.Model):
    email = models.EmailField(max_length=75)
    name = models.CharField(blank=True, max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateField()
    comment = models.TextField(blank=True)

    def __unicode__(self):
        return self.email


class ContactForm(ModelForm):

    class Meta:
        model = ContactLog
        exclude = ('timestamp', 'comment')

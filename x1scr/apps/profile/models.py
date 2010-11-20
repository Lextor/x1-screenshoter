from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(choices=(('Male', 'Male'), ('Female', 'Female')), blank=True, null=True, max_length=6)

    def __unicode__(self):
        return '' #self.user.username

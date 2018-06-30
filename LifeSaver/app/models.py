from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class HelperUser(models.Model):
    orgName = models.CharField(max_length=100, blank=True, null=True)
    contactNumber = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.orgName

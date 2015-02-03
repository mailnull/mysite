from django.db import models
from django.contrib import admin

class RawStatus(models.Model):
    rawmode = models.TextField(max_length=10)
    rawtemp = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

admin.site.register(RawStatus)

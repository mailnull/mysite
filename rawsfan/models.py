from django.db import models
from django.contrib import admin

class RawStatus(models.Model):
    rawmode = models.CharField(max_length=3)
    rawtemp = models.CharField(max_length=2,blank=True)
    timestamp = models.DateTimeField()
    rawtemp1 = models.CharField(max_length=2,default="25")
    room = models.CharField(max_length=4,unique=True)
    rm_en = models.CharField(max_length=4,unique=True)

class RawStatusAdmin(admin.ModelAdmin):
    list_display = ('room','rm_en','timestamp','rawmode','rawtemp')
    
admin.site.register(RawStatus,RawStatusAdmin)

from django.db import models
from django.contrib import admin

# Create your models here.

class LightStatus(models.Model):
    lg_rm_zh = models.CharField(max_length=4,unique=True)
    lg_status = models.CharField(max_length=8,default="dengGuan")
    lg_room = models.CharField(max_length=4,unique=True)
    lg_flag=models.CharField(max_length=1)

class LightStatusAdmin(admin.ModelAdmin):
    list_display = ('lg_rm_zh','lg_room','lg_flag','lg_status')

admin.site.register(LightStatus,LightStatusAdmin)

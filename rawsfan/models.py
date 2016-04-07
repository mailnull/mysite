# _*_ coding:UTF-8 _*_
from django.db import models
from django.contrib import admin

class RawStatus(models.Model):
    rawmode = models.CharField(u"状态模式",max_length=3,help_text=u'制热|制冷')
    rawtemp = models.CharField(max_length=2,verbose_name=u"温度",blank=True)
    timestamp = models.DateTimeField(verbose_name=u"时间")
    rawtemp1 = models.CharField(max_length=2,verbose_name=u"默认温度",default="25")
    room = models.CharField(max_length=4,verbose_name=u"房间名称",unique=True)
    rm_en = models.CharField(max_length=4,verbose_name=u"房间英文",unique=True)

    def __unicode__(self):
    	return self.rm_en
    class Meta:
    	verbose_name = u'空调'
    	verbose_name_plural = u"空调"

class RawStatusAdmin(admin.ModelAdmin):
    list_display = ('room','rm_en','timestamp','rawmode','rawtemp')
    
admin.site.register(RawStatus,RawStatusAdmin)

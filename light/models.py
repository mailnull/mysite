# _*_ coding:UTF-8 _*_
from django.db import models
from django.contrib import admin

# Create your models here.

class LightStatus(models.Model):
    lg_rm_zh = models.CharField(max_length=4,verbose_name=u"房间名称",unique=True)
    lg_status = models.CharField(max_length=8,verbose_name=u"状态英文",default="dengGuan")
    lg_room = models.CharField(max_length=4,verbose_name=u"房间名称英文",unique=True)
    lg_flag=models.CharField(max_length=1,verbose_name=u"状态")
    def __unicode__(self):
        return self.lg_room
    class Meta:
    	verbose_name = u'照明'
    	verbose_name_plural =u'照明'

class espSertime(models.Model):
	Sertime = models.CharField(max_length=4)
	class Meta:
		verbose_name = u'ESP时间'
		verbose_name_plural =u"ESP时间"
	
		
class LightStatusAdmin(admin.ModelAdmin):
    list_display = ('lg_rm_zh','lg_room','lg_flag','lg_status')

class espSertimeAdmin(admin.ModelAdmin):
	list_display = ("Sertime",)
admin.site.register(LightStatus,LightStatusAdmin)
admin.site.register(espSertime,espSertimeAdmin)

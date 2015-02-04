# _*_ coding:UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django import template
from mysite import control,rawscontrol
from django.template import RequestContext
import datetime
from rawsfan.models import RawStatus as raw

def time(reauest):
    for p in raw.objects.filter(rm_en="KTkt"):
        pass
    t1=p.timestamp.replace(tzinfo=None)+datetime.timedelta(hours=8)
    t1=t1.strftime("%m月%d日%H:%M")
    t2 =datetime.datetime.now().strftime("%H:%I")
    dic={'t1':t1,'t2':t2}
    return render_to_response('time.html',dic)
	
	

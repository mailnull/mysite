# _*_ coding:UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import template
from rawsfan import rawscontrol
from rawsfan.code import cold_code , heat_code
from rawsfan.models import RawStatus as rawstatus

def kongtiao(request):
    p = rawstatus.objects.all()
    for i in p :
        wendu = i.rawtemp
        fanmode = i.rawmode
        wendu1 = i.rawtemp1
        dic = {'fan_mode':fanmode,'wendu':wendu,'de_wendu':wendu1}
    if request.method == "POST":
        CON = rawscontrol.rawscontrol()
        if 'AC_on_cold' in request.POST:
            
            CMD=request.POST['AC_on_cold']
            decode=cold_code[int(CMD)-17]
            CON.command(decode)
            ret=CMD
            p = rawstatus.objects.get(id=1)
            p.rawtemp =ret
            p.rawmode="制冷/"
            p.save()
            return HttpResponse(ret)
        elif "AC_on_heat" in request.POST:
            CMD=request.POST['AC_on_heat']
            decode=heat_code[int(CMD)-17]
            CON.command(decode)
            ret=CMD
            p = rawstatus.objects.get(id=1)
            p.rawtemp=ret
            p.rawmode="制暖/"
            p.save()
            return HttpResponse(ret)
        elif request.POST.get('AC_Off',''):
            CON.command("7B84E01F")
            p = rawstatus.objects.get(id=1)
            p.rawmode="关机"
            p.rawtemp=""
            p.save()
            return HttpResponse(p.rawmode)


    return render_to_response('kongtiao.html',dic)

# Create your views here.

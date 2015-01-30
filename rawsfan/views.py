# _*_ coding:UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django import template
from rawsfan import rawscontrol
from rawsfan.code import cold_code , heat_code
from rawsfan.models import RawStatus as rawstatus

list_1 = [u'关机',u'制暖/']
list_2 = [u'关机',u'制冷/']
def kongtiao(request):
    p = rawstatus.objects.all()
    for i in p :
        wendu = i.rawtemp
        fanmode = i.rawmode
        wendu1 = i.rawtemp1
    dic = {'fan_mode':fanmode,'wendu':wendu,'de_wendu':wendu1}
    if request.method == "POST":
        CON = rawscontrol.rawscontrol()
        #制冷
        if 'AC_on_cold' in request.POST:
            p = rawstatus.objects.get(id=1)
            CMD=request.POST['AC_on_cold']
            #任何模式下温度改变或模式为（“关机”或”制暖“）
            if (p.rawmode in list_1) or int(CMD) != int(p.rawtemp):

                decode=cold_code[int(CMD)-17]
                CON.command(decode)
                p.rawtemp =CMD
                p.rawmode="制冷/"
                p.save()
                return HttpResponse(p.rawtemp)
            return HttpResponse(p.rawtemp)
        #制暖
        elif "AC_on_heat" in request.POST:
            p = rawstatus.objects.get(id=1)
            CMD=request.POST['AC_on_heat']

            if (p.rawmode in list_2) or int(CMD) != int(p.rawtemp):
                decode=heat_code[int(CMD)-17]
                CON.command(decode)
                p.rawtemp = CMD 
                p.rawmode="制暖/"
                p.save()
                return HttpResponse(p.rawtemp)
            return HttpResponse(p.rawtemp)
        #关机
        elif request.POST.get('AC_Off',''):
            p = rawstatus.objects.get(id=1)
            if p.rawmode != u'关机':
                CON.command("7B84E01F")
                p.rawmode="关机"
                p.rawtemp=""
                p.save()
                return HttpResponse(p.rawmode)
            return HttpResponse(p.rawmode)


    return render_to_response('kongtiao.html',dic)

# Create your views here.

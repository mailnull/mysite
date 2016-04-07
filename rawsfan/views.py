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
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
list_1 = [u'关机',u'制暖/']
list_2 = [u'关机',u'制冷/']

@login_required(login_url='/login/')
@csrf_exempt
def index(request):
    p_kt = rawstatus.objects.all()
    p = rawstatus.objects.get(id=1)    
    wendu = p.rawtemp
    fanmode =p.rawmode
    wendu1 = p.rawtemp1
    room = p.room
    rm_en = p.rm_en
    dic_index = {'fan_mode':fanmode,'wendu':wendu,'de_wendu':wendu1,'room':room,'rm_en':rm_en,'kt_status':p_kt,'username':request.user.username}
    return render_to_response('kongtiao.html',dic_index)

@login_required(login_url='/login/')
@csrf_exempt
def kongtiao(request,room_CMD):
    p = rawstatus.objects.all()
    pk_room = rawstatus.objects.filter(rm_en=room_CMD)
    for i in pk_room:
        kt_rm_en = i.rm_en
        #kt_room= i.room
        kt_mode = i.rawmode
        kt_temp = i.rawtemp
    if room_CMD == kt_rm_en:
        if request.method == "POST":
            CON=rawscontrol.rawscontrol()
            req_room = request.POST.get('room','')
            if req_room == kt_rm_en:
                if kt_mode == u'关机':
                    i.timestamp=datetime.datetime.now()
                else:
                    pass
                if "AC_on_cold" in request.POST:
                    CMD=request.POST['AC_on_cold']
                    if (kt_mode in list_1) or int(CMD) != int(kt_temp):
                        decode=cold_code[int(CMD)-17]
                        CON.command(decode)
                        i.rawtemp= CMD
                        i.rawmode="制冷/"
                        i.save()
                       # times=i.timestamp.replace(tzinfo=None)#+datetime.timedelta(hours=8)
                        times=i.timestamp.strftime("%m月%d日%H:%M")
                        jsons=json.dumps({"kt_temp":i.rawtemp,"up_time":times},ensure_ascii=False)
                        return HttpResponse(jsons,content_type="application/json")
                    return HttpResponse(i.rawtemp)
                elif "AC_on_heat" in request.POST:
                    CMD=request.POST['AC_on_heat']
                    if (kt_mode in list_2) or int(CMD) != int(kt_temp):
                        decode =heat_code[int(CMD)-17]
                        CON.command(decode)
                        i.rawtemp=CMD
                        i.rawmode="制暖/"
                        i.save()
                        #times=i.timestamp.replace(tzinfo=None)#+datetime.timedelta(hours=8)
                        times=i.timestamp.strftime("%m月%d日%H:%M")
                        jsons=json.dumps({"kt_temp":i.rawtemp,"up_time":times},ensure_ascii=False)
                        return HttpResponse(jsons,content_type="application/json")
                    return HttpResponse(i.rawtemp)
                elif request.POST.get('AC_Off'):
                    if kt_mode != u'关机':
                        CON.command("7B84E01F")

                        i.rawtemp=""
                        i.rawmode="关机"
                        i.save()
                        return HttpResponse(i.rawtemp)
                    return HttpResponse(i.rawtemp)

        dic = {'rm_en':kt_rm_en,'de_wendu':"25",'kt_status':p,'username':request.user.username}
        return render_to_response('kongtiao.html',dic)
    return HttpResponse(room_CMD)

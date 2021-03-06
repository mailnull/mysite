# _*_ coding:UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.http import HttpResponse
import json
from rawsfan.models import RawStatus as raw
from light.models import LightStatus as lgs 
from light import light_con
from rawsfan import rawscontrol
from rawsfan.code import cold_code , heat_code
import datetime
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def weixin_post(request):
    dic={}
    if request.method == "POST":
        if "cmd" in request.POST:
            req_cmd=request.POST.get("cmd",'')
            #req_cmd=json.loads(req_cmd)
            if req_cmd=="kongtiao":
                p=raw.objects.all()
                for i in p:
                
                    dic[str(i.rm_en)]={"status":i.rawmode,"temp":i.rawtemp}

            elif req_cmd=="light":
                p=lgs.objects.all()
                for i in p:
                    dic[i.lg_room]={"status":i.lg_flag}
        #else:
            #dic={"status":"test"}
        elif "dcontrol" in request.POST:
            req_cmd = request.POST.get("dcontrol",'')
            con=light_con.Control_light(req_cmd)
            room=req_cmd
            p=lgs.objects.get(lg_room=room)
            if p.lg_status ==u'dengKai':
                con.command(CMD=0)
                p.lg_status='dengGuan'
                p.lg_flag="关"
                #ret = "off"
                p.save()
            elif p.lg_status==u'dengGuan':
                con.command(CMD=1)
                p.lg_status='dengKai'
                p.lg_flag='开'
                #ret = "on"
                p.save()
            dic={'room':p.lg_rm_zh,'status':p.lg_flag}
        elif 'room' in request.POST:
            room=request.POST.get('room','')
            p_kt=raw.objects.get(rm_en=room)
            con=rawscontrol.rawscontrol()
            if p_kt.rawmode == u'关机':
                p_kt.timestamp=datetime.datetime.now()
            #else:
            #    pass

            if "AC_on_cold" in request.POST:
                CMD=request.POST.get('AC_on_cold','')
                con.command(cold_code[int(CMD)-17])
                p_kt.rawtemp=CMD
                p_kt.rawmode="制冷/"
                p_kt.save()

            elif "AC_on_heat" in request.POST:
                CMD=request.POST.get('AC_on_heat','')
                con.command(heat_code[int(CMD)-17])
                p_kt.rawtemp=CMD
                p_kt.rawmode="制暖/"
                p_kt.save()

            elif request.POST.get('AC_off'):
                con.command('7B84E01F')
                p_kt.rawtemp=""
                p_kt.rawmode="关机"
                p_kt.save()

            dic={'room':p_kt.room,'status':p_kt.rawmode+p_kt.rawtemp}





        response=json.dumps(dic,ensure_ascii=False)
        return HttpResponse(response)
        return HttpResponse(response,content_type="applecation/json")
    return HttpResponse("Only for POST!")
    




def gettime(request):
    status=request.GET.get("status",'')
    now=datetime.datetime.now()
    now=now.strftime("%H%M")
    
    return HttpResponse(now) 

@csrf_exempt
def check_light_status(request):
    if request.method == "POST":
        lightOfroom=request.POST.get("room",None)
        try:
            p=lgs.objects.get(lg_room=lightOfroom)
            status=p.lg_status
            response={"status":status,"room":lightOfroom}
        except:
               response={"status":"error room name!"}
        response=json.dumps(response,ensure_ascii=False)
        return HttpResponse(response,content_type="applecation/json")
    return HttpResponse("Only for POST!")
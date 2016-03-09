# _*_ coding:UTF-8 _*_
from django.shortcuts import render_to_response
from django.http import HttpResponse
from light.models import LightStatus
#from light import lg_control
from light import light_con
from django.contrib.auth.decorators import login_required
import json

on,off=1,0
@login_required(login_url="/login/")
def index(request):
    p = LightStatus.objects.all()
    dic_index = {'Light_status':p,'room':'KTzm','username':request.user.username}
    return render_to_response('deng_light.html',dic_index)

@login_required(login_url="/login/")
def deng(request,room_CMD):
    p = LightStatus.objects.all()
    p_room = LightStatus.objects.filter(lg_room=room_CMD)
    for i in p_room:
        lg_room = i.lg_room
        lg_status=i.lg_status
    if room_CMD == lg_room:
        if request.method == "POST":
            #lg_control.init()
            req_room=request.POST.get("dcontrol","")
            CON =light_con.Control_light(req_room)
            if req_room == lg_room:
                if lg_status == u'dengKai':
                    CON.command(CMD=off)
                    #lg_control.clean()
                    ret = off
                    i.lg_status="dengGuan"
                    i.lg_flag="关"
                    i.save()
                   # return HttpResponse(ret)
                elif lg_status == u'dengGuan':
                    #lg_control.on()
                    CON.command(CMD=on)
                    ret = on
                    i.lg_status = "dengKai"
                    i.lg_flag="开"
                    i.save()
                return HttpResponse(ret)
        dic = {'Light_status':p,'room':lg_room,'username':request.user.username}
        return render_to_response('deng_light.html',dic)
    return HttpResponse("aaaaaaaaaaaaaaaaa")

def weixin_post(request):
    if request.method=="POST":
        status=LightStatus.objects.all()
        w_dic={}
        for i in status:
            w_dic[i.lg_room]={'status':i.lg_status}
        response=json.dumps(w_dic,ensure_asscii=False)
        return HttpResponse(response,content_type="application/json")



    return HttpResponse("只能POST提交!")




        

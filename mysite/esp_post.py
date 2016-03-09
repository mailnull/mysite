# _*_ coding:UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.http import HttpResponse
import json
#from rawsfan.models import RawStatus as raw
from light.models import LightStatus as lgs
from light.models import espSertime as esptime
from light import light_con
import datetime


#sertime=0
def esp8266_post_light(request):
    if request.method == "POST":
        room = request.POST.get("room","")
        lightOfroom = request.POST.get("lightOfroom","")
        if (not room) or (not lightOfroom):
            response = json.dumps({"status":{"message":"POST data invalid!"}},ensure_ascii=False)
            return HttpResponse(response)
        if check_time():
            response = {"status":{"room":room,"lightOfroom":lightOfroom,
                                  "message":"Now it was still daylight,don`t need to turn on the lights"}}
            response['status'].update(change_at=
                                      datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            if lightOfroom == u"turn_ON":
                p_room = lgs.objects.get(lg_room=room)
                if p_room.lg_status ==u'dengGuan':
                    CON = light_con.Control_light(room)
                    CON.command(CMD=1)
                    p_room.lg_status='dengKai'
                    p_room.lg_flag = "关"
                    p_room.save()
                    response = {"status":{"room":room,"message":p_room.lg_status}}
                    response['status'].update(change_at=
                                      datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    response = {"status":{"room":room,"message":"light already on!"}}
                    response['status'].update(change_at=
                                      datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if request.method == "GET":
        response = {"status":{"message":"Only for post!"}}
    response = json.dumps(response,ensure_ascii=False)
    return HttpResponse(response)
        

def check_daylight():
    now = datetime.datetime.now()
    nowtime = now.strftime('%H%M')
    nowmonth = now.strftime('%m')
    AM = 715
    PM = 1600
    summer = ('5','6','7','8','9',)
    winter = ('1','2','3','4','10','11','12')
    if nowmonth in summer:
        AM=630
        PM=1750
    if int(nowtime)>=AM and int(nowtime)<=PM:
        return True
    return False

def check_signature(request):
    #global sertime
    response="NULLNULL"
    signature=request.GET.get("signature","")
    #cmd=request.GET.get("cmd","")
    p=esptime.objects.get(id=1)
    temp=p.Sertime
    buf=int(signature)^int(temp)
    passwd=1314520
    if buf != passwd:
        response="bad request!"
    else:
        if check_daylight():
            response="Now it was still daylight,don`t need to turn on the lights"
        else:
            p_room=lgs.objects.get(lg_room="KTzm")
            if p_room.lg_status==u'dengGuan':
                CON = light_con.Control_light("KTzm")
                CON.command(CMD=1)
                p_room.lg_status='dengKai'
                p_room.lg_flag = "开"
                p_room.save()
                response="KTzm is on "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                response="light already on!"
    #key=19840104
    #response="temp"+str(temp)+"buf"+str(buf)+"signature"+str(signature)
    return HttpResponse(response) 

def gettime(request):
    status=request.GET.get("status",'')
    now=datetime.datetime.now()
    now=now.strftime("%H%M")
    #global sertime
    p=esptime.objects.get(id=1)
    p.Sertime=now
    p.save()
    #sertime=int(now)
    return HttpResponse(now) 

def cmptime(request):
    #global sertime
    return HttpResponse("")
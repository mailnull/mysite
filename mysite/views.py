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
from rawsfan.models import RawStatus as rawstatus
from light.models import LightStatus
from django.contrib import auth
from django.http import HttpResponseRedirect
#系统信息全局
def sysinfo_proc(request):
    now = datetime.datetime.now()
    timeofme="%.19s" %now
    file = open("/sys/class/thermal/thermal_zone0/temp","r")
    temp = float(file.read())/1000
    file.close()
    ftemp = "%.2f" %temp
    ip= request.META['REMOTE_ADDR']
    agent=request.META['HTTP_USER_AGENT']
    
    return {
            'sys_date': timeofme,
            'cpu_temp': ftemp,
            'ipadd': ip,
            'useragent': agent
    }

def index(request):
    dic =""
    p_kt = rawstatus.objects.all()
    p_lg = LightStatus.objects.all()
    #dic= {"Light_status":p_lg,"kt_status":p_kt}
    if request.user.is_authenticated():
        dic= {"Light_status":p_lg,"kt_status":p_kt,'username':request.user.username}
        #return render_to_response('index-.html',dic)
    else:
        dic= {"Light_status":p_lg,"kt_status":p_kt}
        #return render_to_response('index-.html',dic)
	
    return render_to_response('index-.html',dic)
    
	
	

def light(request):
	fp = open("/var/run/deng.pid","r")
	lightflg = int(fp.read())
	fp.close()
	if lightflg == 1:
		ret = 'dengGuan'
		lightstatus = "关"
	else:
		ret = 'dengKai'
		lightstatus = "开"
	dic = {'d_conimg':ret,'lightstatus':lightstatus}
	if request.method == 'POST':
		control.init()
		if request.POST.get("dcontrol",''):
			if lightflg == 1:
				control.on()
				control.flagwriteon()
				ret = "1"
				return HttpResponse(ret)
			else:
				control.off()
				control.clean()
				control.flagwriteoff()
				ret = "0"
				return HttpResponse(ret)
	return render_to_response('deng.html',dic)

def diandeng(request):
    imgsrc2="onkai.jpg" 
    fp = open("/var/run/deng.pid","r")
    flagg = int(fp.read())
    fp.close()
    if flagg == 1:
        imgsrc2 = "offguan.jpg"
    else:
        imgsrc2 = "onkai.jpg"

    if request.method == 'POST':
        control.init()
        if request.POST.get("dcontrol.x",''):
            if flagg == 1:
                control.on()
                control.flagwriteon()
                return render_to_response('diandeng.html',{'d_conimg': 'onkai.jpg' },
                        context_instance=RequestContext(request,processors=[sysinfo_proc]))
            else:
                control.off()
                control.clean()
                control.flagwriteoff()
                return render_to_response('diandeng.html',{'d_conimg': 'offguan.jpg' },
                        context_instance=RequestContext(request,processors=[sysinfo_proc]))

    return render_to_response('diandeng.html',{ 'd_conimg': imgsrc2 },
                context_instance=RequestContext(request,processors=[sysinfo_proc]))

def rawsfancon(request):
    codefan="7B84E01F"
    msg=""
    if request.method == "POST":
        if 'AC_on_col' in request.POST:
            CON=rawscontrol.rawscontrol()
            CMD=request.POST['AC_on_col']
            CON.command(CMD)
            msg ="空调已打开"
            return render_to_response('rawsfan.html',{ 'rawsfan': msg },
                    context_instance=RequestContext(request,processors=[sysinfo_proc]))
        elif 'AC_on_heat' in request.POST:
            CON=rawscontrol.rawscontrol()
            CMD=request.POST['AC_on_heat']
            CON.command(CMD)
            msg ="空调已打开"
            return render_to_response('rawsfan.html',{ 'rawsfan': msg },
                    context_instance=RequestContext(request,processors=[sysinfo_proc]))
        elif request.POST.get('7B84E01F',''):
            CON=rawscontrol.rawscontrol()
            CON.command(codefan)
            msg="空调已关"
            return render_to_response('rawsfan.html',{ 'rawsfan': msg },
                    context_instance=RequestContext(request,processors=[sysinfo_proc]))
        
    return render_to_response('rawsfan.html',{ 'rawsfan': "" },
                context_instance=RequestContext(request,processors=[sysinfo_proc]))

def login_view(request):
    url_name= request.GET.get('next',"")
    if request.method == "POST":
        username= request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            if url_name :
        	    return HttpResponseRedirect(url_name)
            else:
                return HttpResponseRedirect('/')
    	else:
            resp_dic={'username':username,'password':"",'errmsg':u"用户名或者密码错误！"}
            return render_to_response('login.html',resp_dic)
    resp_dic={'username':u"输入用户名",'password':u"请输入密码"}
    return render_to_response('login.html',resp_dic)

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def readtemp(request):
	try:
		from mysite import serial_control as s
	except:
		return HttpResponse("import serial error")

	client = s
	client.send("123456")
	temp=s.readser()
	if (temp):
		return HttpResponse(s) 
	else:
		return HttpResponse("read error")
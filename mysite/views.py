# _*_ coding:UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django import template
from django.template import RequestContext
import datetime



def hello(request):
    return HttpResponse("Hello world")

#def current_datetime(request):
 #   now = datetime.datetime.now()
  #  timeofme="%s" %now
   # return render_to_response('current_datetime.html', {'current_date': timeofme})
#def cpu_temp(request):
 #   file = open("/sys/class/thermal/thermal_zone0/temp","r")
  #  temp = float(file.read())/1000
   # file.close()
    #ftemp = "%.2f" %temp
    #return   render_to_response('cpu_temp.html', {'cpu_temp': ftemp})
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

def show(requset,num):
    num = int(num)
    num = str(num)
    msg = "what your input is:"+num
    return HttpResponse(msg)

def mailnull(requset,num1,num2):
    num1 = str(num1)
    num2 = unichr(num2)
    msg = "the frist param:"+num1+"the second:"+num2
    return HttpResponse(msg)
def index(request):
    return render_to_response('sysinfo.html',
            context_instance=RequestContext(request,processors=[sysinfo_proc]))

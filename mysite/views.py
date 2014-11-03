from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    timeofme="%s" %now
    return render_to_response('current_datetime.html', {'current_date': timeofme})
def cpu_temp(request):
    file = open("/sys/class/thermal/thermal_zone0/temp","r")
    temp = float(file.read())/1000
    file.close()
    ftemp = "%.2f" %temp
    return   render_to_response('cpu_temp.html', {'cpu_temp': ftemp})


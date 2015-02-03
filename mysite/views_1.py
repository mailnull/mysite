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
	
	

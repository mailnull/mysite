from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from mysite.views import hello,current_datetime,cpu_temp
from rawsfan import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$',views.kongtiao),
                      )
urlpatterns+=staticfiles_urlpatterns()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from mysite.views import hello,current_datetime,cpu_temp
from light import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    #url(r'^(.+)/$',views.kongtiao),
    url(r'^$',views.index,name='index'),
    url(r'^(.+)/$',views.deng),
    #url(r'^weixin_post/$',views.weixin_post),
                      )
urlpatterns+=staticfiles_urlpatterns()

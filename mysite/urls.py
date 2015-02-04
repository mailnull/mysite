from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.views import login,logout
#from mysite.views import hello,current_datetime,cpu_temp
from mysite import views,views_1
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^kongtiao/',include('rawsfan.urls')),
    url(r'^light/',include('light.urls')),
    url(r'^login/$',views.login_view),
    url(r'^logout/$',views.logout_view),
    url(r'^admin/', include(admin.site.urls)),
    (r'^$',views.index),
    #(r'^diand/$',views.diandeng),
    #(r'^rawsfan/$',views.rawsfancon),
    #(r'^lights/$',views.light),
    url(r'^time/$',views_1.time),
                      )
urlpatterns+=staticfiles_urlpatterns()

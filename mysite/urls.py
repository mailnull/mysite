from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.views import login,logout
#from mysite.views import hello,current_datetime,cpu_temp
from mysite import views,views_1,weixin_post,esp_post
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^kongtiao/',include('rawsfan.urls')),
    url(r'^light/',include('light.urls',namespace='light')),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^$',views.index),
    #(r'^diand/$',views.diandeng),
    #(r'^rawsfan/$',views.rawsfancon),
    #(r'^lights/$',views.light),
    url(r'^time/$',views_1.time),
    url(r'^weixin_post/$',weixin_post.weixin_post),
    url(r'^check_light_status/$',weixin_post.check_light_status), 
    #url(r'^esp_post/$',esp_post.esp8266_post_light),
    url(r'^gettime/$',esp_post.gettime),
    url(r'^cmptime/$',esp_post.cmptime),
    url(r'^check/$',esp_post.check_signature),
                      )
urlpatterns+=staticfiles_urlpatterns()

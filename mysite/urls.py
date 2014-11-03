from django.conf.urls import patterns, include, url
from django.contrib import admin
#from mysite.views import hello,current_datetime,cpu_temp
from mysite import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    (r'^$',views.hello ),
    (r'^hello/$',views.hello),
    ('^time/$',views.current_datetime),
    (r'^temp/$',views.cpu_temp ),
)

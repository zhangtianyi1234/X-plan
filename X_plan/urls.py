#encoding:utf-8
#导入django相关包
from django.conf.urls import patterns, include, url

#导入djangoadmin用户管理模块
from django.contrib import admin
admin.autodiscover()

#导入项目相关包
from X_plan.views import *
 
urlpatterns = patterns('',
    (r'^$',homepage),
    (r'^login/$',login),
    (r'^register/$',register),
    (r'^globe/$',globe),
    (r'^listall/$',listall),
        # Examples:
    # url(r'^$', 'X_plan.views.home', name='home'),
    #url(r'^X_plan/', include('X_plan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

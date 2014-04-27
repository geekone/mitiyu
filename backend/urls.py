# -*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from backend import views

urlpatterns = patterns('',
    url(r'^$',views.index,name="index"),    #后台管理首页
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/login/$', views.admin_login),
    url(r'^accounts/logout/$', views.admin_logout),
    url(r'^linklist$',views.linklist),
)
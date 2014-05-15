# -*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from guess import views

urlpatterns = patterns('',
    url(r'^$',views.index,name="index"),    #竞猜首页
    url(r'^addquestion$',views.question_add),   #添加问题
    url(r'^questions$',views.question_list),    #问题列表
    url(r'^matchyps$',views.matchyp_list),      #亚盘列表
    url(r'^addmatchyp$',views.matchyp_add),   #添加亚盘
    url(r'^matchbds$',views.matchbd_list),      #波胆列表
    url(r'^addmatchbd$',views.matchbd_add),      #添加波胆
    url(r'^matchdxs$',views.matchdx_list),      #大小球列表
    url(r'^addmatchdx$',views.matchdx_add),      #添加大小球


)
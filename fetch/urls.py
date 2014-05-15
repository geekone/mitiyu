# -*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from fetch import  views
urlpatterns = patterns('',
    url(r'^$',views.index),
    url(r'^fetch8bo',views.fetch_8bo),
)

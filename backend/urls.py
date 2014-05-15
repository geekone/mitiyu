# -*- coding:utf-8 -*-
from django.conf.urls import patterns,url
from backend import views

urlpatterns = patterns('',
    url(r'^$',views.index,name="index"),    #后台管理首页
    url(r'^categories$',views.category_list),        #分类列表
    url(r'^addcategory$',views.category_add),        #添加分类
    url(r'^movies$',views.movie_list),               #视频列表
    url(r'^addmovie$',views.movie_add),              #添加视频
    url(r'^articles$',views.article_list),          #文章列表
    url(r'^addarticle$',views.article_add),        #添加文章
    url(r'^links$',views.link_list),                #友情列表
    url(r'^addlink$',views.link_add),               #添加友情

    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/login/$', views.admin_login),
    url(r'^accounts/logout/$', views.admin_logout),

)
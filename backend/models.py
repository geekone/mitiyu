#-*- coding:utf-8 -*-
import datetime
from django.db import models

#保存友情链接
class Link(models.Model):
    link_id = models.AutoField(primary_key=True)               #自增链接id
    link_url = models.CharField(max_length=255)  #链接url
    link_name = models.CharField(max_length=255)    #链接名
    # link_image  = models.CharField(max_length=255)  #链接图象
    # link_target = models.CharField(max_length=25)   #键接打开方式
    link_description  = models.CharField(max_length=255)  #说明
    # link_visible = models.CharField(max_length=20)    #是否可见
    # link_owner = models.IntegerField()              #链接用户ID
    # link_rating = models.IntegerField()             #链接等级
    # link_updated = models.DateTimeField()           #修改时间
    # link_rel = models.CharField(max_length=255)     #与连接者的关系
    # link_notes = models.TextField()                 #连接注解
    # link_rss  =models.CharField(max_length=255)     # rss

    class Meta:
        db_table = "t_link"

    def __unicode__(self):
        return self.link_name


#分类模型
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)      #英文
    cname = models.CharField(max_length=50)     #中文

    class Meta:
        db_table = "t_category"

    def __unicode__(self):
        return self.name

#视频模型
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)            #视频标题
    content = models.TextField()                        #视频内容
    category = models.ForeignKey(Category,related_name='category_movie')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="t_movie"

    def __unicode__(self):
        return self.title

#文章模型
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)        #文章标题
    content = models.TextField()                    #文章内容
    category = models.ForeignKey(Category,related_name='category_article')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_article"

    def __unicode__(self):
        return self.title





#新闻临时模型,抓取用的
class ArticleTmpModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)        #标题
    url = models.CharField(max_length=255)          #远程地址
    content = models.TextField()                    #内容
    created = models.IntegerField()                 #建立日期
    pubdate = models.CharField(max_length=45)       #发布日期
    fromto = models.CharField(max_length=45)        #来自哪里

    class Meta:
        db_table = "t_articles_tmp"

    def __unicode__(self):
        return self.title
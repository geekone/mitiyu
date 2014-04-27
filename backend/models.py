#-*- coding:utf-8 -*-
from django.db import models

#保存友情链接
class Link(models.Model):
    link_id = models.AutoField(primary_key=True)               #自增链接id
    link_url = models.CharField(max_length=255)  #链接url
    link_name = models.CharField(max_length=255)    #链接名
    link_image  = models.CharField(max_length=255)  #链接图象
    link_target = models.CharField(max_length=25)   #键接打开方式
    link_description  = models.CharField(max_length=255)  #说明
    link_visible = models.CharField(max_length=20)    #是否可见
    link_owner = models.IntegerField()              #链接用户ID
    link_rating = models.IntegerField()             #链接等级
    link_updated = models.DateTimeField()           #修改时间
    link_rel = models.CharField(max_length=255)     #与连接者的关系
    link_notes = models.TextField()                 #连接注解
    link_rss  =models.CharField(max_length=255)     # rss

    class Meta:
        db_table = "t_link"

    def __unicode__(self):
        return self.user_id


#新闻临时表
class ArticleTmpModel(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    content = models.TextField()
    created = models.IntegerField()
    pubdate = models.CharField(max_length=45)
    fromto = models.CharField(max_length=45)

    class Meta:
        db_table = "t_articles_tmp"

    def __unicode__(self):
        return self.title
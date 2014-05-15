# -*- coding:utf-8 -*-
from django.db import models

#8bo 波国家模型
class Country8bo(models.Model):
    id = models.AutoField(primary_key=True)
    cid = models.IntegerField()                 #国家ID
    en = models.CharField(max_length=45)        #英文
    cn = models.CharField(max_length=45)        #中国
    tw = models.CharField(max_length=45)        #繁体
    type = models.SmallIntegerField()           #区别 1 足球 2 篮球
    class Meta:
        db_table = "country_8bo"

    def __unicode__(self):
        return self.cn


#8bo 联赛模型
class League8bo(models.Model):
    id = models.AutoField(primary_key=True)
    lid = models.IntegerField()                 #联赛ID
    color = models.CharField(max_length=45)
    en = models.CharField(max_length=45)        #英文
    cn = models.CharField(max_length=45)        #中国
    tw = models.CharField(max_length=45)        #繁体
    type = models.SmallIntegerField()           #区别 1 足球 2 篮球
    class Meta:
        db_table = "league_8bo"

    def __unicode__(self):
        return self.cn


#8bo 球队模型
class Team8bo(models.Model):
    id = models.AutoField(primary_key=True)
    tid = models.IntegerField()                 #球队ID
    en = models.CharField(max_length=45)        #英文
    cn = models.CharField(max_length=45)        #中国
    tw = models.CharField(max_length=45)        #繁体
    type = models.SmallIntegerField()           #区别 1 足球 2 篮球
    class Meta:
        db_table = "team_8bo"

    def __unicode__(self):
        return self.cn








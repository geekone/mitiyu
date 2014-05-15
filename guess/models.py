# -*- coding:utf-8 -*-
from django.db import models

# 文字问答模型
class Question(models.Model):
    id = models.AutoField(primary_key=True)         #自增链接ID
    title = models.CharField(max_length=255)        #问题
    answer = models.SmallIntegerField()             # 0, 1 (y ,no)
    created = models.DateTimeField()                #添加时间
    class Meta:
        db_table = "guess_question"

    def __unicode__(self):
        return self.title

#亚盘
class Matchyp(models.Model):
    yp_id = models.AutoField(primary_key=True)
    yp_matchid = models.IntegerField()              #比赛ID
    # yp_sr = models.IntegerField()
    yp_t = models.DateTimeField()
    yp_t1d = models.IntegerField()
    yp_t1GBn = models.CharField(max_length=100)     #主队
    yp_t2d = models.IntegerField()
    yp_t2GBn = models.CharField(max_length=100)     #客队

    class Meta:
        db_table = "guess_matchyp"

    def __unicode__(self):
        return self.yp_matchid

#波胆
class Matchbd(models.Model):
    bd_id = models.AutoField(primary_key=True)
    bd_matchid = models.IntegerField()
    # bd_sr = models.IntegerField()
    bd_t = models.DateTimeField()
    bd_t1d = models.IntegerField()
    bd_t1GBn = models.CharField(max_length=100)
    bd_t2d = models.IntegerField()
    bd_t2GBn = models.CharField(max_length=100)

    class Meta:
        db_table = "guess_matchbd"

    def __unicode__(self):
        return self.bd_matchid


#大小
class Matchdx(models.Model):
    dx_id = models.AutoField(primary_key=True)
    dx_matchid = models.IntegerField()
    # dx_sr = models.IntegerField()
    dx_t = models.DateTimeField()
    dx_t1d = models.IntegerField()
    dx_t1GBn = models.CharField(max_length=100)
    dx_t2d = models.IntegerField()
    dx_t2GBn = models.CharField(max_length=100)

    class Meta:
        db_table = "guess_matchdx"

    def __unicode__(self):
        return self.dx_matchid









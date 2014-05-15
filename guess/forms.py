#! /usr/bin/env python
#coding=utf-8
__author__ = 'Administrator'
from django import forms

#问题的Form
class QuestionForm(forms.Form):
    title = forms.CharField(label=u'问题')

#亚盘的form
class MatchypForm(forms.Form):
    matchid = forms.CharField(label=u'亚盘比赛ID')
    matchtime = forms.CharField(label=u'比赛时间')
    t1id = forms.CharField(label=u'主队编号')
    t1name = forms.CharField(label=u'主队名称')
    t2id = forms.CharField(label =u'客队编号')
    t2name = forms.CharField(label=u'客队名称')

#波胆form
class MatchbdForm(forms.Form):
    matchid = forms.CharField(label=u'波胆比赛ID')
    matchtime = forms.CharField(label=u'比赛时间')
    t1id = forms.CharField(label=u'主队编号')
    t1name = forms.CharField(label=u'主队名称')
    t2id = forms.CharField(label =u'客队编号')
    t2name = forms.CharField(label=u'客队名称')

#大小球form
class MatchdxForm(forms.Form):
    matchid = forms.CharField(label=u'大小球比赛ID')
    matchtime = forms.CharField(label=u'比赛时间')
    t1id = forms.CharField(label=u'主队编号')
    t1name = forms.CharField(label=u'主队名称')
    t2id = forms.CharField(label =u'客队编号')
    t2name = forms.CharField(label=u'客队名称')

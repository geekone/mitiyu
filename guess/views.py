# -*-coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import time
from guess.forms import QuestionForm, MatchypForm, MatchbdForm, MatchdxForm
from guess.models import Question, Matchyp, Matchbd, Matchdx


def index(request):
    return render_to_response("guess/index.html");



def question_list(request):
    _questions = Question.objects.all()
    return render_to_response("guess/question_list.html",{'questions':_questions})

#文字问题操作
def question_add(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            question_Model = Question()
            question_Model.title =cd['title']
            question_Model.answer = 0
            question_Model.created = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            question_Model.save()
            return HttpResponseRedirect("/guess")
    else:
        form = QuestionForm()
        c = {'form':form}
        return render_to_response("guess/question_add.html",c,context_instance=RequestContext(request))

#亚盘列表
def matchyp_list(request):
    _matchs = Matchyp.objects.all()
    return render_to_response("guess/matchyp_list.html",{'matchs':_matchs})

#亚盘添加
def matchyp_add(request):
    if request.method == "POST":
        form = MatchypForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            yp = Matchyp()
            yp.yp_matchid = cd['matchid']
            yp.yp_t = cd['matchtime']
            yp.yp_t1d = cd['t1id']
            yp.yp_t2d = cd['t2id']
            yp.yp_t1GBn = cd['t1name']
            yp.yp_t2GBn = cd['t2name']
            yp.save()
            return HttpResponseRedirect("/guess/matchyps")
    else:
        form = MatchypForm()
        c = {'form':form}
        return render_to_response("guess/matchyp_add.html",c,context_instance=RequestContext(request))

#波胆列表
def matchbd_list(request):
    _matchs = Matchbd.objects.all()
    return render_to_response("guess/matchbd_list.html",{'matchs':_matchs})

def matchbd_add(request):
    if request.method == "POST":
        form = MatchbdForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            bd = Matchbd()
            bd.bd_matchid = cd['matchid']
            bd.bd_t = cd['matchtime']
            bd.bd_t1d = cd['t1id']
            bd.bd_t2d = cd['t2id']
            bd.bd_t1GBn = cd['t1name']
            bd.bd_t2GBn = cd['t2name']
            bd.save()
            return HttpResponseRedirect("/guess/matchbds")
    else:
        form = MatchbdForm()
        c = {"form":form}
        return render_to_response("guess/matchbd_add.html",c,context_instance=RequestContext(request))




#大小球列表
def matchdx_list(request):
    _matchs = Matchdx.objects.all()
    return render_to_response("guess/matchdx_list.html",{"matchs":_matchs})


#添加大小球
def matchdx_add(request):
    if request.method == "POST":
        form = MatchdxForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dx = Matchdx()
            dx.dx_matchid = cd['matchid']
            dx.dx_t = cd['matchtime']
            dx.dx_t1d = cd['t1id']
            dx.dx_t2d = cd['t2id']
            dx.dx_t1GBn = cd['t1name']
            dx.dx_t2GBn = cd['t2name']
            dx.save()
            return HttpResponseRedirect("/guess/matchdxs")
    else:
        form = MatchdxForm()
        c = {'form':form}
        return render_to_response("guess/matchdx_add.html",c,context_instance=RequestContext(request))

#-*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


@login_required(login_url='/backend/accounts/login/')
def index(request):
    return render_to_response("backend/index.html")


#登录
def admin_login(request):
    if request.method == "POST":
        _username = request.POST["username"]
        _password = request.POST["password"]
        user = authenticate(username=_username,password=_password)
        if user is not None:
            if user.is_active:
                login(request,user)
                _next = request.GET['next']
                return HttpResponseRedirect(_next)
            else:
                return HttpResponse("用户登录出错")
    return render_to_response("backend/login.html",None,context_instance=RequestContext(request))


def admin_logout(request):
    logout(request)
    return HttpResponseRedirect("/backend")


@login_required(login_url='/backend/accounts/login/')
def linklist(request):
    return render_to_response("backend/linklist.html")


#文章代表
def articletmplist(request):
    return render_to_response("admin/articletmplist.html")
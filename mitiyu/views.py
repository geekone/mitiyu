#-*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.views.decorators.csrf import csrf_protect


def index(request):
    return render_to_response("index.html",None,context_instance=RequestContext(request))





# # @csrf_protect
# def login_view(request):
#     _username = request.POST["username"]
#     _password = request.POST["password"]
#     user = authenticate(username=_username,password=_password)
#     if user is not None:
#         login(request,user)
#         print request.user
#     return render_to_response("index.html",{'request':request})


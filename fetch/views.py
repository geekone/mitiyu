# -*- coding:utf-8 -*-
'''
    抓取的控制
'''
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

#抓取首页
def index(reqeust):
    return render_to_response("backend/fetch_index.html")

def fetch_8bo(request):
    return HttpResponseRedirect("/fetch")
#-*- coding:utf-8 -*-
import time
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from backend.forms import CategoryForm, MovieForm, LinkForm, ArticleForm
from backend.models import Category, Article, Movie


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


#分类列表
def category_list(request):
    _categories = Category.objects.all()
    return render_to_response("backend/category_list.html",{'categories':_categories})

#添加分类
def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            category = Category()
            category.name = cd['name']
            category.cname = cd['cname']
            # print request.POST['aname']
            category.save()
            return HttpResponseRedirect("/backend/categories")
    else:
        form = CategoryForm()
        c = {'form':form}
        return render_to_response("backend/category_add.html",c,context_instance=RequestContext(request))

#视频列表
def movie_list(request):
    _movies = Movie.objects.all()
    return render_to_response("backend/movie_list.html",{'movies':_movies})

#添加视频
def movie_add(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            movie = Movie()
            movie.title = cd['title']
            movie.content = cd['content']
            movie.created =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            movie.save()
            return HttpResponseRedirect("/backend/movies")
    else:
        form = MovieForm()
        c = {'form':form}
        return render_to_response("backend/movie_add.html",c,context_instance=RequestContext(request))

#文章列表
def article_list(request):
    _articles = Article.objects.all()
    return render_to_response("backend/article_list.html",{'articles':_articles})


#添加文章
def article_add(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            article = Article()
            article.title = cd['title']
            article.content = cd['content']
            article.created = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            article.save()
            return HttpResponseRedirect("/backend/articles")
    else:
        form = ArticleForm()
        c = {'form':form}
        return render_to_response("backend/article_add.html",c,context_instance=RequestContext(request))





#友情连接列表
@login_required(login_url='/backend/accounts/login/')
def link_list(request):
    return render_to_response("backend/link_list.html")

#添加友情连接
def link_add(request):
    if request.method == "POST":
        pass
    else:
        form = LinkForm()
        c = {'form':form}
        return render_to_response("backend/link_add.html",c,context_instance=RequestContext(request))


#文章代表
def articletmplist(request):
    return render_to_response("admin/articletmplist.html")






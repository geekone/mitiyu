#-*- coding:utf-8 -*-
import time
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from backend.forms import CategoryForm, MovieForm, LinkForm, ArticleForm
from backend.models import Category, Article, Movie, Link


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
            category.save()
            return HttpResponseRedirect("/backend/categories")
    else:
        form = CategoryForm()
        c = {'form':form}
        return render_to_response("backend/category_add.html",c,context_instance=RequestContext(request))

#修改分类
def category_edit(request,category_id):
    if request.method == "POST":
        _id = request.POST['categoryid']
        _name = request.POST['name']
        _cname = request.POST['cname']
        category = Category.objects.get(pk=_id)
        category.name = _name
        category.cname = _cname
        category.save()
        return HttpResponseRedirect("/backend/categories")
    else:
        category = Category.objects.get(pk=category_id)
        c = {'category':category}
        return render_to_response("backend/category_edit.html",c,context_instance=RequestContext(request))


#删除分类，会级联删除分类下的
def category_delete(request,category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return HttpResponseRedirect("/backend/categories")


#文章列表
def article_list(request):
    _articles = Article.objects.all()
    return render_to_response("backend/article_list.html",{'articles':_articles})

#添加文章
def article_add(request):
    if request.method == 'POST':
        _title = request.POST['title']
        _content = request.POST['content']
        article = Article()
        article.title = _title
        article.content = _content
        article.category = Category.objects.get(pk=request.POST['categoryid'])
        article.save()
        return HttpResponseRedirect("/backend/articles")
    else:
        _categories = Category.objects.all()
        c = {'categories':_categories}
        return render_to_response("backend/article_add.html",c,context_instance=RequestContext(request))

#修改文章
def article_edit(request,article_id):
    if request.method == "POST":
        _id = request.POST['articleid']
        _title = request.POST['title']
        _content = request.POST['content']
        _categoryid = request.POST['categoryid']
        article = Article.objects.get(pk = _id)
        article.title = _title
        article.content = _content
        article.category = Category.objects.get(pk=_categoryid)
        article.save()
        return HttpResponseRedirect("/backend/articles")
    else:
        _categories = Category.objects.all()
        article = Article.objects.get(pk=article_id)
        c = {'article':article,'categories':_categories}
        return render_to_response("backend/article_edit.html",c,context_instance=RequestContext(request))


#删除文章
def article_delete(request,article_id):
    _article = Article.objects.get(pk=article_id)
    _article.delete()
    return HttpResponseRedirect("/backend/articles")





# #添加文章
# def article_add(request):
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             article = Article()
#             article.title = cd['title']
#             article.content = cd['content']
#             article.created = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#             article.save()
#             return HttpResponseRedirect("/backend/articles")
#     else:
#         form = ArticleForm()
#         c = {'form':form}
#         return render_to_response("backend/article_add.html",c,context_instance=RequestContext(request))





####################  视频 ######################
def movie_list(request):
    _movies = Movie.objects.all()
    return render_to_response("backend/movie_list.html",{'movies':_movies})

#添加视频
def movie_add(request):
    if request.method == "POST":
        _title = request.POST['title']
        _content = request.POST['content']
        movie = Movie()
        movie.title = _title
        movie.content = _content
        movie.category = Category.objects.get(pk=request.POST['categoryid'])
        movie.save()
        return HttpResponseRedirect("/backend/movies")
    else:
        _categories = Category.objects.all()
        c = {'categories':_categories}
        return render_to_response("backend/movie_add.html",c,context_instance=RequestContext(request))

#修改
def movie_edit(request,movie_id):
    if request.method == 'POST':
        _id = request.POST['movieid']
        _title = request.POST['title']
        _content = request.POST['content']
        _categoryid = request.POST['categoryid']
        movie = Movie.objects.get(pk= _id)
        movie.title = _title
        movie.content = _content
        movie.category = Category.objects.get(pk=_categoryid)
        movie.save()
        return HttpResponseRedirect("/backend/movies")
    else:
        _categories = Category.objects.all()
        movie = Movie.objects.get(pk=movie_id)
        c = {'movie':movie,'categories':_categories}
        return render_to_response("backend/movie_edit.html",c,context_instance=RequestContext(request))

#删除
def movie_delete(request,movie_id):
    _movie = Movie.objects.get(pk=movie_id)
    _movie.delete()
    return HttpResponseRedirect("/backend/movies")


#################  friendlink ######################
def link_list(request):
    _links = Link.objects.all()
    return render_to_response("backend/link_list.html",{'links':_links})

#添加
def link_add(request):
    if request.method == 'POST':
        _link_url = request.POST['link_url']
        _link_name = request.POST['link_name']
        _link_description = request.POST['link_description']
        link = Link()
        link.link_name = _link_name
        link.link_url = _link_url
        link.link_description = _link_description
        link.save()
        return HttpResponseRedirect("/backend/links")
    else:
        return render_to_response("backend/link_add.html",None,context_instance=RequestContext(request))

#修改
def link_edit(request,link_id):
    if request.method == 'POST':
        _id = request.POST['linkid']
        _link_url = request.POST['link_url']
        _link_name = request.POST['link_name']
        _link_description = request.POST['link_description']
        link = Link.objects.get(pk = _id)
        link.link_url = _link_url
        link.link_name = _link_name
        link.link_description = _link_description
        link.save()
        return HttpResponseRedirect("/backend/links")
    else:
        link = Link.objects.get(pk = link_id)
        c = {'link':link}
        return render_to_response('backend/link_edit.html',c,context_instance=RequestContext(request))

#删除
def link_delete(request,link_id):
    link = Link.objects.get(pk = link_id)
    link.delete()
    return HttpResponseRedirect("/backend/links")



# #友情连接列表
# @login_required(login_url='/backend/accounts/login/')
# def link_list(request):
#     return render_to_response("backend/link_list.html")



# #添加友情连接
# def link_add(request):
#     if request.method == "POST":
#         pass
#     else:
#         form = LinkForm()
#         c = {'form':form}
#         return render_to_response("backend/link_add.html",c,context_instance=RequestContext(request))


#文章代表
def articletmplist(request):
    return render_to_response("admin/articletmplist.html")






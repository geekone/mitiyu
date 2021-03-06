# -*- coding:utf-8 -*-
from django import forms

#分类Form
class CategoryForm(forms.Form):
    name = forms.CharField(label=u'名称')

#视频Form
class MovieForm(forms.Form):
    title = forms.CharField(label=u'标题')
    content = forms.CharField(label=u'内容',widget=forms.Textarea)

#文章的Form
class ArticleForm(forms.Form):
    title = forms.CharField(label=u'标题')
    content = forms.CharField(label=u'内容',widget=forms.Textarea)

#友情链接Form
class LinkForm(forms.Form):
    link_url = forms.CharField(label=u'url地址')
    link_name = forms.CharField(label=u'友情链接')
    link_description = forms.CharField(label=u'说明',widget=forms.Textarea)



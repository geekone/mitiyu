# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mitiyu.views.index', name='homeindex'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^guess/',include('guess.urls')),        #竞猜URL
    url(r'^backend/',include('backend.urls')),        #后台管理URL

)

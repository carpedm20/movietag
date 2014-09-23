#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movietag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.movie_list, name='movie_list'),
    url(r'^search/$', views.movie_search_default, name='movie_search_default'),
    url(r'^search/(?P<text>[\w]+)/$', views.movie_search, name='movie_search'),
)

# -*- coding: utf-8 -*-
"""
title              :urls
description        :urls for blog app
date               :04.10.16
"""
from django.conf.urls import url, include
from .views import IndexView, PostView, AboutView, PostsListView, ContactView

__author__ = 'Vitold Komorovski'

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='post'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^posts/', PostsListView.as_view(), name='posts'),
    url(r'^send_message/', ContactView.as_view(), name='send_message'),
    url(r'^$', IndexView.as_view(), name='main'),
]

# -*- coding: utf-8 -*-
"""
title              :urls
description        :urls for blog app
date               :04.10.16
"""
from django.conf.urls import url, include
from .views import IndexView

__author__ = 'Vitold Komorovski'

urlpatterns = [
    url(r'^', IndexView.as_view(), name='main'),
    url(r'^comments/', include('django_comments.urls')),
]
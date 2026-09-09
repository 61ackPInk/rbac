"""
-*- coding: utf-8 -*-
@File  : urls.py
@Author: 61ackPink
@Date: 2026/9/5 13:49
@Desc : 
"""
from django.urls import path, include, re_path

from apps.com.view.img import ImgView, ImgFileView

urlpatterns = [
    # 图片上传、删除
    path('img/', ImgView.as_view(), name='img'),
    path('img/<int:pk>/', ImgView.as_view(), name='img_detail'),
    # re_path(r'^img/file/(?P<file_name>.+)/$', ImgFileView.as_view(), name='img_file')
    re_path(r'^img/(?P<file_name>.+)$', ImgFileView.as_view(), name='img_file')
]
"""
-*- coding: utf-8 -*-
@File  : urls.py
@Author: 61ackPink
@Date: 2026/9/5 13:49
@Desc : 
"""
from django.urls import path, include

from apps.com.view.img import ImgView

urlpatterns = [
    # 图片上传、删除
    path('img/', ImgView.as_view(), name='img'),
]
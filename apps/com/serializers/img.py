"""
-*- coding: utf-8 -*-
@File  : img.py
@Author: 61ackPink
@Date: 2026/9/5 10:31
@Desc : 
"""

from rest_framework import serializers
from apps.com.models import Img

class ImgSeria(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'
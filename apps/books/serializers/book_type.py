"""
-*- coding: utf-8 -*-
@File  : book_type.py
@Author: 61ackPink
@Time : 2026/8/28 10:21
@Desc : book_type序列化器
"""

from rest_framework import serializers
from apps.books.models import BookType


class BookTypeSeria(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = '__all__'


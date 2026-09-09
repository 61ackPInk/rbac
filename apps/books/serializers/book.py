"""
-*- coding: utf-8 -*-
@File  : book.py
@Author: 61ackPink
@Time : 2026/9/4 17:29
@Desc : book序列化器
"""
from rest_framework import serializers
from apps.books.models import Book

class BookSeria(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
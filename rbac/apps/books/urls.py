"""
-*- coding: utf-8 -*-
@File  : urls.py
@Author: 61ackPink
@Time : 2026/8/28 10:05
@Desc : 
"""

from django.urls import path, include

from apps.books.views.book_type import BookTypeListView, BookTypeView
from apps.books.views.book import BookListView, BookView

urlpatterns = [
    # 图书类型
    path('type/', BookTypeListView.as_view(), name="book_type_list"),
    path('type/<int:pk>/', BookTypeView.as_view(), name="book_type"),
    # 图书
    path('book/', BookListView.as_view(), name="book_list"),
    path('book/<int:pk>/', BookView.as_view(), name="book"),
]
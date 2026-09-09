"""
-*- coding: utf-8 -*-
@File  : book.py
@Author: 61ackPink
@Time : 2026/9/4 17:40
@Desc : 图书视图
"""

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.books.models import Book
from apps.books.serializers import BookSeria
from common.utils.log import log

class BookListView(GenericAPIView):
    serializer_class = BookSeria
    queryset = Book.objects.all()

    def get(self, request):
        # 查询数据
        res = self.get_queryset()
        # 序列化
        seria = BookSeria(instance=res, many=True)
        # 返回数据
        return Response(seria.data)

    def post(self, request, *args, **kwargs):
        # 获取数据
        data = request.data
        seria = BookSeria(data=data)
        # 校验数据
        seria.is_valid(raise_exception=True)
        # 保存
        seria.save()
        return Response("添加成功")

class BookView(GenericAPIView):
    serializer_class = BookSeria
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        # 查询
        obj = self.get_object()
        seria = BookSeria(instance=obj, many=False)
        return Response(seria.data)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        # 前端传来的新数据
        data = request.data
        # 序列化器同时传递新data 和 obj == 修改
        seria = BookSeria(instance=obj, data=data, partial=True)
        seria.is_valid(raise_exception=True)
        # 保存
        seria.save()
        return Response(seria.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response("删除成功")
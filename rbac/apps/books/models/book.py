"""
-*- coding: utf-8 -*-
@File  : book.py
@Author: 61ackPink
@Time : 2026/8/28 10:05
@Desc : 图书模型
"""

from django.db import models
from apps.books.models.book_type import BookType

class Book(models.Model):
    num = models.CharField(max_length=10, unique=True, verbose_name="图书编号")
    name = models.CharField(max_length=50, unique=True, verbose_name="图书名字")
    # 价格，最多十位数，小数两位
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="图书价格")
    # book_type 图书类型-> 一个对象类型
    book_type = models.ForeignKey(BookType, on_delete=models.SET_NULL, null=True, verbose_name="图书类型")
    status = models.BooleanField(default=False, verbose_name="借阅状态")

    def __str__(self):
        return f"{self.num} - {self.name} - {self.price} - {self.book_type} - {self.status}"

    class Meta:
        db_table = "book"
        verbose_name = "图书表"
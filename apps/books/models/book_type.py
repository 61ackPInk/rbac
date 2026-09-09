"""
-*- coding: utf-8 -*-
@File  : book_type.py
@Author: 61ackPink
@Time : 2026/8/28 10:06
@Desc : 图书类型模型
"""

from django.db import models

class BookType(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="图书类型")
    description = models.CharField(max_length=50, verbose_name="描述信息")

    def __str__(self):
        return f"{self.name} --- {self.id}"

    class Meta:
        # 表名
        db_table = "book_type"
        verbose_name = "图书类型表"
        verbose_name_plural = verbose_name


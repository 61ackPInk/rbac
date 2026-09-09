"""
-*- coding: utf-8 -*-
@File  : img.py
@Author: 61ackPink
@Time : 2026/9/5 10:19
@Desc :
"""

from django.db import models

class Img(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    file = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    folder = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = "com_img"
        verbose_name = "图片表"

    def __str__(self):
        return f"{self.name} - {self.file.name}"
"""
-*- coding: utf-8 -*-
@File  : img.py
@Author: 61ackPink
@Date: 2026/9/5 11:28
@Desc : 
"""
import os
import uuid

from django.http import FileResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.com.serializers import ImgSeria
from apps.com.models import Img
from common.utils.log import log
from common.utils import my_utils

from rbac import settings


class ImgView(GenericAPIView):
    serializer_class = ImgSeria
    queryset = Img.objects.all()

    # 增加
    def post(self, request, *args, **kwargs):
        """
        :param request:
        """
        file = request.data.get('file')
        # 获取file的后缀，重新命名
        suffix = file.name[file.name.rfind('.'):]
        file.name = str(uuid.uuid4()) + suffix
        log.info(file.name)
        seria = ImgSeria(data=request.data)
        seria.is_valid(raise_exception=True)
        # 文件大小判断
        if file.size > 1024 * 1024 * 5: # 5M
            return Response(data="上传文件不能超过5M", status=status.HTTP_400_BAD_REQUEST)
        # 格式判断
        if file.content_type not in ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']:
            return Response(data="文件格式不支持", status=status.HTTP_400_BAD_REQUEST)

        seria.validated_data["name"] = request.user.username
        seria.save()
        return Response(data=seria.data, status=status.HTTP_200_OK)

    # 删除
    def delete(self, request, *args, **kwargs):
        """
        接收参数 file_name
        """
        # 获取删除图片的名字
        img_id = kwargs.get('pk')
        if not img_id:
            return Response("缺少图片id", status=status.HTTP_400_BAD_REQUEST)

        try:
            # 获取图片对象
            img_obj = Img.objects.get(pk=img_id)
        except Img.DoesNotExist:
            return Response("图片不存在", status=status.HTTP_400_BAD_REQUEST)

        if img_obj.file:
            file_path = os.path.join(settings.MEDIA_ROOT, img_obj.file.name)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    log.info(f"删除成功- {file_path}")
                except Exception as e:
                    log.error(f"删除失败: {str(e)}")
                    return Response(f"删除失败： {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                log.info(f"文件不存在 - {file_path}")
            img_obj.delete()
            log.info(f"图片删除成功, ID: {img_id}, 名称: {img_obj.name}")
        return Response("删除成功", status=status.HTTP_200_OK)


class ImgFileView(GenericAPIView):
    def get(self, request, file_name):
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        try:
            file = open(file_path, 'rb')
            return FileResponse(file)
        except FileNotFoundError:
            return Response("图片不存在", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("异常", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
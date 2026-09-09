"""
-*- coding: utf-8 -*-
@File  : my_utils.py
@Author: 61ackPink
@Date: 2026/9/5 17:30
@Desc : 
"""
import os
import uuid
from rbac import settings
from common.utils.log import log

# 获取uuid
def get_uuid():
    return uuid.uuid1()


# 列表转树
# def list_to_tree(data:list) -> list:
#     """
#     data 格式：
#         [{'id': 1, 'pid': 0, 'name': '用户管理', 'url': 'https://www.baidu.com'}]
#     """
#     # 创建容器树
#     tree_list = []
#     # 获取id列表
#     id_list = [item.get('id') for item in data]
#     # 转换为字典，key=id, value=obj
#     zipped = zip(id_list, data)
#     # 转为字典
#     dic_data = dict(zipped)
#     for item in data:
#         parent = dic_data.get(item['pid'])
#         if parent is None:
#             tree_list.append(item)
#         else:
#             if parent.get('children') is None:
#                 parent['children'] = []
#             parent['children'].append(item)
#     return tree_list

# 列表转树
def list_to_tree(data: list) -> list:
    """
    将列表转换为树形结构，时间 O(n)

    Args:
        data: 列表，每个元素需包含 'id' 和 'pid' 字段

    Returns:
        树形结构列表（根节点）
    """
    if not data:
        return []

    # 构建 id → item 映射
    node_map = {item['id']: item for item in data}

    tree = []
    for item in data:
        parent = node_map.get(item['pid'])
        if parent is None:
            tree.append(item)
        else:
            parent.setdefault('children', []).append(item)

    return tree


# 删除图片的方法
def delete_file(name):
    if name is None or name == "":
        return
    file_path = os.path.join(settings.MEDIA_ROOT, name)
    log.critical(f'file_path:{file_path}')

    if os.path.exists(file_path):
        log.info('删除了？？')
        os.remove(file_path)

if __name__ == '__main__':
    data: list = [
        {'id': 1, 'pid': 0, 'name': '用户管理', 'url': 'https://www.baidu.com'},
        {'id': 2, 'pid': 0, 'name': '菜单管理', 'url': 'https://www.baidu.com'},
        {'id': 3, 'pid': 1, 'name': '新增用户', 'url': 'https://www.baidu.com'},
        {'id': 4, 'pid': 1, 'name': '删除用户', 'url': 'https://www.baidu.com'},
        {'id': 5, 'pid': 3, 'name': '新增菜单', 'url': 'https://www.baidu.com'},
        {'id': 6, 'pid': 2, 'name': '删除菜单', 'url': 'https://www.baidu.com'}
    ]
    print(list_to_tree(data))
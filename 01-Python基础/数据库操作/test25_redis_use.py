# encoding=utf-8

"""
使用redis操作redis数据库的功能，增删改查
author：LBL
date:2023-2-13
"""
import redis


# 程序主入口
if __name__ == "__main__":
    """ redis第三方模块可操作redis数据库，安装 pip install redis ，
    操作过程：1、创建连接对象
            2、执行操作（添加、查询、删除）
    """
    # 创建redis连接对象实例（对象）
    try:
        rs = redis.Redis()
        # 添加操作
        result = rs.set('name', 'xiaowang')
        print(result)
        # 查询操作
        name = rs.get('name')
        print(name)

    except Exception as e:
        print(e)


# encoding=utf-8

"""
元组类型数据使用,
author：LBL
date:2023-2-8
"""

if __name__ == "__main__":
    # 定义元组，元组与列表使用基本一致，但元组内元素不能修改,只有一个元素的元组定义需要加,
    test_tuple1 = ()
    test_tuple2 = (30,)
    test_tuple3 = ("孙权", 23, 1.76)
    # 元组与列表互相转化
    test_list = list(test_tuple3)
    test_tuple4 = tuple(test_list)
    print(test_tuple4)




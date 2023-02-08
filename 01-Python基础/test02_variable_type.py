# encoding=utf-8

"""
基本变量类型,变量互相转化,格式化字符串
author：LBL
date:2023-2-8
"""

if __name__ == "__main__":
    # 不同变量类型与拆包
    my_int, my_float, my_str, my_None, *my_bool= [24, 123.2, "张三", None, True, False]

    """ 格式化字符串:% """
    # %d代表整数。   %95d代表五位整数，不足用0补齐
    print("%d    %05d" % (my_int,my_int))
    # %f代表浮点数。  %.2f代表保留两位小数
    print("%.2f" % my_float)
    # %s代表字符串
    print("%s" % my_str)

    """ 变量类型转换"""
    n1 = int("12")      # 字符串转整数       12
    n2 = int("1011",2)  # 二进制字符串转整数  11
    n3 = float("11.1")  # 字符串转浮点数
    s1 = str(10)        # 其他类型转字符串
    b1 = bool(11)       # 其他类型转布尔类型，只要不是0都是True






